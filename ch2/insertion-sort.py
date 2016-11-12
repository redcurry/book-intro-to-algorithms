def main():
    seq = [31, 41, 59, 26, 41, 58]
    print seq
    insertion_sort(seq)
    print seq
    insertion_sort_reverse(seq)
    print seq

def insertion_sort(a):
    for j in range(len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

def insertion_sort_reverse(a):
    for j in range(len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

main()
