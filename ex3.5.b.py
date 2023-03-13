import timeit
import random
import matplotlib.pyplot as plt

# Inefficient implementation
def priority_queue_inefficient(arr):
    queue = []
    for elem in arr:
        queue.append(elem)
        queue.sort(reverse=True)
        queue.pop()
    return queue

# Efficient implementation
import heapq
def priority_queue_efficient(arr):
    queue = []
    for elem in arr:
        heapq.heappush(queue, elem)
        if len(queue) > 10:
            heapq.heappop(queue)
    return queue


def time_priority_queue(func, arr):
    start = timeit.default_timer()
    func(arr)
    end = timeit.default_timer()
    return end - start

def run_experiment():
    arr = [random.randint(1, 100000) for _ in range(1000)]
    inefficient_times = []
    efficient_times = []
    num_measurements = 100
    for _ in range(num_measurements):
        inefficient_time = time_priority_queue(priority_queue_inefficient, arr)
        efficient_time = time_priority_queue(priority_queue_efficient, arr)
        inefficient_times.append(inefficient_time)
        efficient_times.append(efficient_time)

    print(f"Aggregate results over {num_measurements} measurements:")
    print(f"Inefficient implementation: {sum(inefficient_times)/num_measurements:.8f} seconds (min: {min(inefficient_times):.8f} seconds)")
    print(f"Efficient implementation: {sum(efficient_times)/num_measurements:.8f} seconds (min: {min(efficient_times):.8f} seconds)")


    plt.hist(inefficient_times,  alpha=0.5, label='Inefficient')
    plt.hist(efficient_times, alpha=0.5, label='Efficient')
    plt.legend(loc='upper right')
    plt.set_xlabel('Execution Time (seconds)')
    plt.set_ylabel('Frequency')
    plt.show()






run_experiment()
