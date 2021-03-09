class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ans = [];
        for i in range(len(A[0])):
            switch = [];
            for j in range(len(A)):
                switch.append(A[j][i])
            ans.append(switch);
        return ans;
