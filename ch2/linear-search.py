def main():
    seq = [31, 41, 59, 26, 41, 48]
    print seq
    print find(seq, 48)

# Loop invariant:
#
# At the start of each iteration of the for loop,
# the variable i is None if v does not appear
# in the subarray a[0..j - 1], or i is such that
# v = a[i]. Note that if j < 0, a is an empty array.

def find(a, v):
    
    i = None

    # When j is 0, the subarray is empty,
    # so no element is equal to v, so i is None.

    # When j is greater than zero, if v is equal to a[j],
    # i is set to j and immediately finishes the loop,
    # so this property is always true.

    for j in range(len(a)):
        if v == a[j]:
            i = j
            break

    # If the break never happens, i is None,
    # which is correct because it means the array
    # never contained the element v.

    return i

main()
