def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(L, R):
    merged = []
    li = 0
    ri = 0
    while li < len(L) and ri < len(R):
        if L[li] <= R[ri]:
            merged.append(L[li])
            li = li + 1
        else:
            merged.append(R[ri])
            ri = ri + 1
    if li < len(L):
        merged.extend(L[li:])
    if ri < len(R):
        merged.extend(R[ri:])
    return merged


def main():
    import random

    unsorted = []
    for i in range(100):
        unsorted.append(random.randrange(1, 100))

    print(unsorted)
    print('\n')
    print(merge_sort(unsorted))


if __name__ == '__main__':
    main()
