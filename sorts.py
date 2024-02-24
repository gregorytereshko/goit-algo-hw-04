import random
import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


sizes = [100, 1000, 10000]
arrays = {size: [random.randint(0, size) for _ in range(size)] for size in sizes}

def time_sorting_algorithm(algorithm, arr):
    if algorithm is not None:
      return timeit.timeit(lambda: algorithm(arr.copy()), number=1)
    else:
      return timeit.timeit(lambda: arr.copy().sort(), number=1)

for size, arr in arrays.items():
    print(f"Array size: {size}")
    print(f"Insertion sort time: {time_sorting_algorithm(insertion_sort, arr):.6f} seconds")
    print(f"Merge sort time: {time_sorting_algorithm(merge_sort, arr):.6f} seconds")
    print(f"Timsort (sorted) time: {time_sorting_algorithm(sorted, arr):.6f} seconds")
    print(f"Timsort (sort) time: {time_sorting_algorithm(None, arr):.6f} seconds")
    print()
