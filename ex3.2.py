import json
import time
import matplotlib.pyplot as plt


with open("ex2data.json") as f:
    data = json.load(f)
    
with open("ex2tasks.json") as f:
    tasks = json.load(f)


def binary_search(arr, x, start, end, mid):
    if start > end:
        return False
    
    if arr[mid] == x:
        return True
    
    if arr[mid] > x:
        return binary_search(arr, x, start, mid-1, (start+mid-1)//2)
    else:
        return binary_search(arr, x, mid+1, end, (mid+1+end)//2)


best_midpoints = []
for task in tasks:
    start = 0
    end = len(data) - 1
    best_time = float('inf')
    best_midpoint = None
    
    for i in range(start, end+1):
        mid = (start+i)//2
        start_time = time.perf_counter()
        found = binary_search(data, task, start, end, mid)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        
        if found and elapsed_time < best_time:
            best_time = elapsed_time
            best_midpoint = mid
        
    best_midpoints.append(best_midpoint)


plt.scatter(tasks, best_midpoints)
plt.title("Initial Midpoint vs. Performance")
plt.xlabel("Search Task")
plt.ylabel("Best Initial Midpoint")
plt.show()


