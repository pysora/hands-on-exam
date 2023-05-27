def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

numbers = [230, 171, 95, 500, 67, 4]
sorted_numbers = bubble_sort_descending(numbers)
print(f"Sorted numbers in descending order: {sorted_numbers}")
