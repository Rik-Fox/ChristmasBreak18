import numpy as np


def mergepresorted(A, B):

    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] < B[0]:
        A_split = np.array_split(A, [1, n])
        C = np.concatenate(mergepresorted(A_split[1], B), A_split[0])
        return C
    else:
        B_split = np.array_split(B, [1, n])
        C = np.concatenate((mergepresorted(A, B_split[1]), B_split[0]))
        return C


def mergesort(A, B, n):
    if n == 1:
        C = mergepresorted(A, B)
        return C
    else:
        m = np.int_(n/2)
        A_split = np.array_split(A, 2)
        B_split = np.array_split(A, 2)
        C = mergepresorted(mergesort(A_split[0], A_split[1], m),
                           mergesort(B_split[0], B_split[1],  m))
        return C
