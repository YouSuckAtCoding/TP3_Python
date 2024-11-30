def partition(array, low, high):
    pivot = array[high];
    window_start = low - 1;

    for i in range(low, high):
        if array[i] <= pivot:
            window_start+=1;
            array[i], array[window_start] = array[window_start], array[i];

    window_start+=1;
    array[window_start], array[high] = array[high], array[window_start];
    return window_start;


def quickSort(array, low, high):
    if low <= high:
        window_start = partition(array, low, high);
        quickSort(array, window_start + 1, high);
        quickSort(array, low, window_start - 1);

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
