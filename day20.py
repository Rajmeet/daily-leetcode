# 2661. First Completely Painted Row or Column
# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

# Return the smallest index i at which either a row or a column will be completely painted in mat.

 

# Example 1:
# image explanation for example 1

# Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
# Output: 2
# Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        path = [[False] * cols for _ in range(rows)]
        
        rowCount = [0] * rows
        colCount = [0] * cols
        
        positionMap = {}
        
        for i in range(rows):
            for j in range(cols):
                positionMap[mat[i][j]] = (i, j)

        for index in range(len(arr)):
            number = arr[index]
            pos = positionMap.get(number)
            
            if pos is not None:
                r, c = pos
                
                path[r][c] = True
                rowCount[r] += 1
                colCount[c] += 1
                
                if rowCount[r] == cols or colCount[c] == rows:
                    return index
        
        return -1  
    
print(Solution().firstCompleteIndex([1,3,4,2], [[1,4],[2,3]]))