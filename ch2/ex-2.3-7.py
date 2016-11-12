import sys
import random
import math

def main():
    a = [random.randint(1, 100) for x in range(10)]
    print a[3], a[7]
    s = a[3] + a[7]
    print sum_exists(a, s)

def sum_exists(a, s):
    merge_sort(a)
    print a
    print s
    i = 0
    j = len(a) - 1
    while 0 <= i < j < len(a):
        print i, j, a[i] + a[j]
        if a[i] + a[j] == s:
            return True
        elif s < (a[i] + a[j]):
            i += 1
        else:
            i -= 1
            j -= 1
    return False


def merge_sort(a):
    return merge_sort_rec(a, 0, len(a) - 1)

def merge_sort_rec(a, p, r):
    if p < r:
        q = int(math.floor((p + r) / 2.0))
        merge_sort_rec(a, p, q)
        merge_sort_rec(a, q + 1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    L = a[p:(q + 1)]
    R = a[(q + 1):(r + 1)]
    L.append(sys.maxint)
    R.append(sys.maxint)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if (L[i] <= R[j]):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1


main()
