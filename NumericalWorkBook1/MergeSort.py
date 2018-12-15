import numpy as np


def mergepresorted(A, B):

    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] < B[0]:
        return np.insert(mergepresorted(A[1:-1], B), 0, A[0])
    else:
        return np.insert(mergepresorted(A, B[1:-1]), 0, B[0])


def mergesort(A, B, n):
    if n == 1:
        C = mergepresorted(A, B)
        return C
    else:
        m = np.int_(n/2)
        C = mergepresorted(mergesort(A[0:m], A[m+1:n], m), mergesort(B[0:m], B[m+1:n], m))
        return C
