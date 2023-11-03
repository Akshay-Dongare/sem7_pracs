'''Write a program for analysis of quick sort by using deterministic and randomized variants.'''
import random

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less = [x for x in arr[:-1] if x <= pivot]
        greater = [x for x in arr[:-1] if x > pivot]
        return deterministic_quick_sort(less) + [pivot] + deterministic_quick_sort(greater)
    
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        less = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        greater = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
        return randomized_quick_sort(less) + [pivot] + randomized_quick_sort(greater)

arr = list(map(int, input("Enter array elements for sorting (comma seperated): ").split(',')))
print("Unsorted Array (Entered by user):", arr)
sorted_deterministic = deterministic_quick_sort(arr)
print("Sorted Array (Deterministic Quick Sort):", sorted_deterministic)
sorted_randomized = randomized_quick_sort(arr)
print("Sorted Array (Randomized Quick Sort):", sorted_randomized)

