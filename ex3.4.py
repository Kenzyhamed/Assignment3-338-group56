import threading
import time
import random

class Queue:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.lock = threading.Lock()
        self.empty = threading.Event()

    def enqueue(self, item):
        while True:
            self.lock.acquire()
            if (self.tail + 1) % self.size != self.head:
                self.buffer[self.tail] = item
                self.tail = (self.tail + 1) % self.size
                self.empty.set()
                self.lock.release()
                return
            else:
                self.lock.release()
                time.sleep(1)

    def dequeue(self):
        while True:
            self.empty.wait()
            self.lock.acquire()
            if self.head != self.tail:
                item = self.buffer[self.head]
                self.head = (self.head + 1) % self.size
                if self.head == self.tail:
                    self.empty.clear()
                self.lock.release()
                return item
            else:
                self.lock.release()
                time.sleep(1)

def producer(queue):
    while True:
        item = random.randint(1, 10)
        time.sleep(item)
        queue.enqueue(item)

def consumer(queue):
    while True:
        item = random.randint(1, 10)
        time.sleep(item)
        print(queue.dequeue())

if __name__ == '__main__':
    size = 10
    q = Queue(size)

    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
