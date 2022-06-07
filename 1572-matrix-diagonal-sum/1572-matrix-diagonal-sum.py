class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        end = len(mat)
        sums = 0
        
        for i in range(end):
            sums += mat[i][i] + mat[i][end-i-1]
        
        if end % 2 != 0:
            sums -= mat[end//2][end//2]
        
        return sums