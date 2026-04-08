#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'canPlaceSecurityCameras' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY grid
#

def canPlaceSecurityCameras(N, grid):
    # Write your code here
    cols = [False] * N
    diag1 = [False] * (2 * N - 1)  # Major diagonals (r - c)
    diag2 = [False] * (2 * N - 1)  # Minor diagonals (r + c)

    def solve(row):
        # Base case: Successfully placed a camera in every row
        if row == N:
            return True

        for col in range(N):
            # Check if cell is blocked (1) or if there's a conflict
            if grid[row][col] == 1:
                continue
                
            d1_idx = row - col + (N - 1)
            d2_idx = row + col
            
            if not cols[col] and not diag1[d1_idx] and not diag2[d2_idx]:
                # Place the camera
                cols[col] = diag1[d1_idx] = diag2[d2_idx] = True
                
                # Recursively try to place the next camera
                if solve(row + 1):
                    return True
                
                # Backtrack: Remove the camera and try the next column
                cols[col] = diag1[d1_idx] = diag2[d2_idx] = False
        
        return False

    return solve(0)
    


if __name__ == '__main__':
    N = int(input().strip())

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = canPlaceSecurityCameras(N, grid)

    print(int(result))
