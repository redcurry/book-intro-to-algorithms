def invMergeSort(a):
    return invMergeSortRec(a, 0, len(a) - 1)

def invMergeSortRec(a, low, high):
    if low < high:
        mid = (low + high) // 2
        return invMergeSortRec(a, low, mid) + \
            invMergeSortRec(a, mid + 1, high) + \
            invMerge(a, low, mid, high)
    else:
        return 0

def invMerge(a, low, mid, high):
    left = a[low:(mid + 1)]
    right = a[(mid + 1):(high + 1)]
    li = 0
    ri = 0
    n_inv = 0
    for i in range(low, high + 1):
        if li < len(left) and (ri >= len(right) or left[li] <= right[ri]):
            a[i] = left[li]
            li += 1
        elif ri < len(right) and (li >= len(left) or right[ri] <= left[li]):
            a[i] = right[ri]
            n_inv += (len(left) - li)
            ri += 1
    return n_inv
