def binary_search(a, v):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if v < a[mid]:
            high = mid - 1
        elif v > a[mid]:
            low = mid + 1
        else:
            return mid
    return -1
