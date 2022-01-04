def partition(arr, begin, end):
    pivot = begin

    for i in range(begin+1, end+1):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[begin] = arr[begin], arr[pivot]
    return pivot

def quicksort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1
    def _quicksort(arr, begin, end):
        if begin >= end:
            return
        pivot = partition(arr, begin, end)
        _quicksort(arr, begin, pivot-1)
        _quicksort(arr, pivot+1, end)
    return _quicksort(arr, begin, end)

arr = [10, 7, 8, 9, 1, 5]
quicksort(arr)
print(arr)