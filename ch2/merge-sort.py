import sys
import random
import math

def main():
    seq = [random.randint(1, 100) for x in range(16)]
    print seq
    merge_sort(seq)
    print seq

def merge_sort(a):
    return merge_sort_rec(a, 0, len(a) - 1)

def merge_sort_rec(a, p, r):
    if p < r:
        q = int(math.floor((p + r) / 2.0))
        merge_sort_rec(a, p, q)
        merge_sort_rec(a, q + 1, r)
        merge2(a, p, q, r)

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

# Exercise 2.3-2
def merge2(a, p, q, r):
    L = a[p:(q + 1)]
    R = a[(q + 1):(r + 1)]
    i = 0
    j = 0
    for k in range(p, r + 1):
        if i >= len(L) or j >= len(R):
            break
        elif (L[i] <= R[j]):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
    if k <= r and i >= len(L):
        for m in range(k, r + 1):
            a[m] = R[j]
            j += 1
    elif k <= r and j >= len(R):
        for m in range(k, r + 1):
            a[m] = L[i]
            i += 1


main()
