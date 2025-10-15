class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        n=len(matrix)
        m=len(matrix[0])
        row,col=[0]*n,[0]*m

        for i in range (n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for k in range(n):
            for l in range(m):
                if row[k]==1 or col[l]==1:
                    matrix[k][l]=0
        return matrix
            

        

        