# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
# Solved
# Hard
# Topics
# Companies
# Hint

# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

#     1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
#     2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
#     3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
#     4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

# Notice that there could be some signs on the cells of the grid that point outside the grid.

# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

# Return the minimum cost to make the grid have at least one valid path.
# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.

# not done
from typing import List
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ans = float('inf')

        n,m = len(grid), len(grid[0])
        q = deque()
        q.append([0,0,0])
        d = {}

        while(q):
            i,j,cost = q.popleft()
            if i<0 or i>= n or j<0 or j>=m: continue
            
            if i == n-1 and j == m-1: 
                ans = min(ans,cost)
                continue

            if (i,j) not in d or d[(i,j)] > cost:
                d[(i,j)] = cost
            else: continue
                

            direction = grid[i][j]

            direction_cost = {1:1,2:1,3:1,4:1}
            direction_cost[direction] = 0

            if direction == 1:
                q.appendleft([i,j+1,cost+direction_cost[1]])
                q.append([i,j-1,cost+direction_cost[2]])
                q.append([i+1,j,cost+direction_cost[3]])
                q.append([i-1,j,cost+direction_cost[4]])


            if direction == 2:
                q.append([i,j+1,cost+direction_cost[1]])
                q.appendleft([i,j-1,cost+direction_cost[2]])
                q.append([i+1,j,cost+direction_cost[3]])
                q.append([i-1,j,cost+direction_cost[4]])

            if direction == 3:
                q.append([i,j+1,cost+direction_cost[1]])
                q.append([i,j-1,cost+direction_cost[2]])
                q.appendleft([i+1,j,cost+direction_cost[3]])
                q.append([i-1,j,cost+direction_cost[4]])

            if direction == 4:
                q.append([i,j+1,cost+direction_cost[1]])
                q.append([i,j-1,cost+direction_cost[2]])
                q.append([i+1,j,cost+direction_cost[3]])
                q.appendleft([i-1,j,cost+direction_cost[4]])

        return ans

print(Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])) # 3
