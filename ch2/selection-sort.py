def main():
    seq = [31, 41, 59, 26, 41, 58]
    print seq
    selection_sort(seq)
    print seq

def selection_sort(a):                       # Times
    for j in range(len(a) - 1):              # n - 1
        min_i = j                            # n - 1
        for i in range(j + 1, len(a)):       # E[1,n-1] t_j
            if a[i] < a[min_i]:              # E[1,n-1] t_j
                min_i = i
        temp = a[j]                          # n - 1
        a[j] = a[min_i]                      # n - 1
        a[min_i] = temp                      # n - 1

# Best-case and worst-case are the same because, even if the array is sorted,
# finding the minimum requires going through the entire array.

# t_j = n - j - 1
# E[1,n-1] t_j = E[1,n-1] (n - j - 1)
#              = n(n - 1) - E[1,n-1] j - (n - 1)
#              = n(n - 1) - [n(n-1)/2 - n] - (n - 1)
#              = n^2 - n - (n^2 - 3n)/2 - (n - 1)
#              = (1/2)n^2 - (7/2)n + 1

# T(n) = (n - 1) + (n - 1) + 2 * [(1/2)n^2 - (7/2)n + 1] + 3 * (n - 1)

main()
