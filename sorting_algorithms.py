# Sorting Algorithms in Python
# A collection of common sorting algorithms for beginners


# --- Bubble Sort ---
# Repeatedly steps through the list, compares adjacent elements,
# and swaps them if they are in the wrong order.
# Time complexity: O(n^2) average and worst case
def bubble_sort(arr):
    arr = arr[:]  # work on a copy so the original is not modified
    n = len(arr)
    for i in range(n):
        # After each pass, the largest unsorted element "bubbles" to its place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# --- Selection Sort ---
# Divides the list into a sorted and unsorted part.
# Repeatedly selects the smallest element from the unsorted part
# and moves it to the end of the sorted part.
# Time complexity: O(n^2) average and worst case
def selection_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# --- Insertion Sort ---
# Builds the sorted list one element at a time by inserting each
# new element into its correct position among the already-sorted elements.
# Time complexity: O(n^2) average and worst case, O(n) best case (already sorted)
def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# --- Merge Sort ---
# A divide-and-conquer algorithm that splits the list in half,
# recursively sorts each half, then merges the two sorted halves.
# Time complexity: O(n log n) in all cases
def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


# --- Quick Sort ---
# A divide-and-conquer algorithm that picks a pivot element and
# partitions the list so that elements smaller than the pivot come
# before it and elements larger come after it, then recursively
# sorts the two partitions.
# Time complexity: O(n log n) average, O(n^2) worst case
def quick_sort(arr):
    arr = arr[:]
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr, low, high):
    if low < high:
        pivot_index = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pivot_index - 1)
        _quick_sort_helper(arr, pivot_index + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    smaller_element_index = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            smaller_element_index += 1
            arr[smaller_element_index], arr[j] = arr[j], arr[smaller_element_index]
    arr[smaller_element_index + 1], arr[high] = arr[high], arr[smaller_element_index + 1]
    return smaller_element_index + 1


# --- Demo ---
if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:", sample)
    print()
    print("Bubble Sort:   ", bubble_sort(sample))
    print("Selection Sort:", selection_sort(sample))
    print("Insertion Sort:", insertion_sort(sample))
    print("Merge Sort:    ", merge_sort(sample))
    print("Quick Sort:    ", quick_sort(sample))
