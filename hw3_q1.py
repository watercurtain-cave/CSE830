def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Generate arrays of different sizes
# sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 100, 500, 1000]
sizes = [(i+1)*10 for i in range(30)]
merge_sort_times = []
insertion_sort_times = []

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    
    start_time = time.time()
    merge_sort(arr.copy())
    end_time = time.time()
    merge_sort_times.append(end_time - start_time)
    
    start_time = time.time()
    insertion_sort(arr.copy())
    end_time = time.time()
    insertion_sort_times.append(end_time - start_time)

merge_sort_times = np.array(merge_sort_times)
insertion_sort_times = np.array(insertion_sort_times)

ratio = insertion_sort_times / merge_sort_times

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(sizes, ratio, label='Merge / Insertion')
# plt.plot(sizes, insertion_sort_times, label='Insertion Sort', marker='x')
plt.xlabel('Array Size (n)')
plt.ylabel('Ratio')
plt.title('Merge Sort vs Insertion Sort Time Rotio')
plt.legend()
plt.grid(True)
plt.savefig('./test.png')
