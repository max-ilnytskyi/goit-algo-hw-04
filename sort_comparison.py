import random
import timeit


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def timsort(arr):
    return sorted(arr)


def create_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]


list_sizes = [100, 1000, 5000, 10000]

for size in list_sizes:
    random_list = create_random_list(size)
    print(f"List Size: {size}")

    merge_sort_time = timeit.timeit(lambda: merge_sort(random_list.copy()), number=10)
    print(f"Merge Sort Time: {merge_sort_time:.4f} seconds")

    if size <= 1000:  # Insertion Sort is too slow for large lists
        insertion_sort_time = timeit.timeit(
            lambda: insertion_sort(random_list.copy()), number=10
        )
        print(f"Insertion Sort Time: {insertion_sort_time:.4f} seconds")
    else:
        print("Insertion Sort Time: Skipped (too slow for large lists)")

    timsort_time = timeit.timeit(lambda: timsort(random_list.copy()), number=10)
    print(f"Timsort (Python's sorted) Time: {timsort_time:.4f} seconds")
    print("-" * 40)
