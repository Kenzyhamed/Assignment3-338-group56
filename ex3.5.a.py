import time
import random
import matplotlib.pyplot as plt

# Inefficient Implementation
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Efficient Implementation
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Generate sorted array of size n
n = 1000
arr = list(range(n))

# Measure time taken to search for random elements using inefficient implementation
linear_times = []
for i in range(100):
    x = random.randint(0, n-1)
    start_time = time.time()
    linear_search(arr, x)
    end_time = time.time()
    linear_times.append(end_time - start_time)

# Measure time taken to search for random elements using efficient implementation
binary_times = []
for i in range(100):
    x = random.randint(0, n-1)
    start_time = time.time()
    binary_search(arr, x)
    end_time = time.time()
    binary_times.append(end_time - start_time)

# Plot distribution of measured values
plt.hist(linear_times, alpha=0.5, label='Linear Search')
plt.hist(binary_times, alpha=0.5, label='Binary Search')
plt.legend(loc='upper right')
plt.ylabel('Frequency')
plt.xlabel('Time(s)')
plt.show()

# Print aggregate of measured values
print("Linear Search Average Time:", sum(linear_times)/len(linear_times))
print("Binary Search Average Time:", sum(binary_times)/len(binary_times))

