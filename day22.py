# 1765. Map of Highest Peak
# Solved
# Medium
# Topics
# Companies
# Hint

# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

#     If isWater[i][j] == 0, cell (i, j) is a land cell.
#     If isWater[i][j] == 1, cell (i, j) is a water cell.

# You must assign each cell a height in a way that follows these rules:

#     The height of each cell must be non-negative.
#     If the cell is a water cell, its height must be 0.
#     Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

#  Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:        
        q = deque()
        m = len(isWater)
        n = len(isWater[0])
        matrix = [[-1] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j, 0))
                    matrix[i][j] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, height = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == -1:
                    # Set height to 1 more than current cell
                    matrix[nr][nc] = height + 1
                    # Add to queue for further exploration
                    q.append((nr, nc, height + 1))

        return matrix

print(Solution().highestPeak([[0,1],[0,0]]))