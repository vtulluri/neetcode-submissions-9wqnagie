class Solution:
    def searchMatrix(self, matrix, target):
        # Staircase search and its o(m+n)
        # i = 0
        # j = len(matrix[0]) - 1
        # # print(j)

        # while i < len(matrix) and j >= 0:
        #     if matrix[i][j] == target:
        #         return True
        #     elif target > matrix[i][j]:
        #         i += 1
        #     else:
        #         j -= 1

        # return False

        # Binary search

        row=len(matrix)
        cols=len(matrix[0])
        print(cols)

        left=0
        right=row*cols-1

        while left<=right:
            mid=(left+right)//2

            r= mid//cols
            c=mid%cols

            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                left=mid+1
            else:
                right=mid-1
        return False
