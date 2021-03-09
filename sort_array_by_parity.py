\class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0 
        end = len(A) - 1
        while start < end:
            if A[start] % 2 > A[end] % 2:
                A[start], A[end] = A[end], A[start] #switch occurs here 
            if A[start] % 2 == 0: #increment start value if even
                start += 1
            if A[end] % 2 == 1: #decrement end value if odd
                end -= 1

        return A
