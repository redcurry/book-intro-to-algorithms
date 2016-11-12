import sys
import math

def main():
    seq = [4, 8, 9, 15, 23, 45, 51, 65, 78, 99]
    print seq
    print binary_search(seq, 4)
    print binary_search(seq, 8)
    print binary_search(seq, 9)
    print binary_search(seq, 15)
    print binary_search(seq, 23)
    print binary_search(seq, 45)
    print binary_search(seq, 51)
    print binary_search(seq, 65)
    print binary_search(seq, 78)
    print binary_search(seq, 99)
    print binary_search(seq, 3)
    print binary_search(seq, 11)
    print binary_search(seq, 50)
    print binary_search(seq, 80)
    print binary_search(seq, 100)

def binary_search(a, v):
    return binary_search_rec(a, v, 0, len(a) - 1)

def binary_search_rec(a, v, low, high):
    if low > high:
        return -1

    if low == high:
        if v == a[low]:
            return low
        else:
            return -1

    mid = (low + high) / 2

    if v < a[mid]:
        return binary_search_rec(a, v, low, mid - 1)
    elif v > a[mid]:
        return binary_search_rec(a, v, mid + 1, high)
    else:
        return mid


# Worst-case: v is not in list
#
# Assume n = 2^k, k >= 0
#
# T(n=1) = O(1)
# T(n) = 1*T(n/2) + O(1) + 0    D(n) = O(1) and C(n) = 0
#      = T(n/2) + c
#
# Using the logic of the tree (p. 35),
# Total = c*lg(n) + c = O(lg n)


main()
