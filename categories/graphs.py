# NUMBER OF ISLANDS
'''
You are given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water).

We need to return the number of islands.

Rules:
1. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
2. You may assume all four edges of the grid are all surrounded by water.

EXAMPLE 1:
Input: grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
Output: 1

EXAMPLE 2:
Input: grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
Output: 3
'''
from collections import deque

class IslandCounter:
    def num_islands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
            
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        self.total_islands = 0
        
        # --- THE SCANNER ---
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "1" and (r, c) not in self.visited:
                    self.total_islands += 1  # We count it!
                    self.spreader(r, c)      # We map it!
                    
        return self.total_islands

    # --- THE SPREADER ---
    def spreader(self, r, c):
        queue = deque()
        
        # Add start point to queue and visited set
        queue.append((r, c))
        self.visited.add((r, c))
        
        directions = {
            'DOWN' : [1,0],
            'UP' : [-1,0],
            'RIGHT' : [0,1],
            'LEFT' : [0,-1]
        }
        
        while queue:
            curr_r, curr_c = queue.popleft()
            
            for dr, dc in directions.values():
                new_r = curr_r + dr
                new_c = curr_c + dc
                
                if (0 <= new_r < self.rows and
                    0 <= new_c < self.cols and
                    self.grid[new_r][new_c] == '1' and
                    (new_r, new_c) not in self.visited):
                    
                    self.visited.add((new_r, new_c))
                    queue.append((new_r, new_c))

# # tests
# grid = [
#   ['1','1','0','0','0'],
#   ['1','1','0','0','0'],
#   ['0','0','1','0','0'],
#   ['0','0','0','1','1']
# ] # -> 3

# island_counter = IslandCounter()
# print(island_counter.num_islands(grid))

# SENIOR APPROACH WITH SINKING PATTERN (BY GEMINI)
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # if grid is empty
        if not grid: return 0
        
        # tuple unpack, if 4x3 grid -> 4 rows, 3 cols
        rows, cols = len(grid), len(grid[0])

        # island counter
        islands = 0
        
        # 1. The Scanner
        for r in range(rows):
            for c in range(cols):
                # if cell is a land spot
                if grid[r][c] == '1':
                    # increment island counter
                    islands += 1
                    # call the spreader
                    self.sink_island(grid, r, c, rows, cols) 
                    
        # return island counter
        return islands

    # 2. The Spreader (DFS Version - often shorter to write than BFS)
    # DFS = DEPTH-FIRST SEARCH
    # BFS = BREADTH-FIRST SEARCH
    def sink_island(self, grid, r, c, rows, cols):
        # Base Case: If we go out of bounds OR hit water ('0'), stop.
        # if row or column are negative or current cell is 'water'
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == '0':
            return
        
        # it can also be written as
        # if not (rows > r >= 0 and cols > c >= 0) or grid[r][c] == '0':
            
        
        # SINK IT! Mark as visited by changing '1' to '0'
        grid[r][c] = '0'
        
        # Recursively sink neighbors (Up, Down, Left, Right)
        # (0, 0) = TOP-LEFT corner of the grid
        # r += 1 as you go DOWN
        # c += 1 as you go RIGHT
        self.sink_island(grid, r + 1, c, rows, cols) # down
        self.sink_island(grid, r - 1, c, rows, cols) # up
        self.sink_island(grid, r, c + 1, rows, cols) # right
        self.sink_island(grid, r, c - 1, rows, cols) # left

# FLOOD COLOR FILL
'''
You are given an image represented by an m x n grid of integers image,
where image[i][j] represents the pixel value (color) of the image.

You are also given three integers:
- sr, sc: The starting row and column of the pixel you clicked on.
- color: The new color you want to paint the region.

The Task Perform a "flood fill". This means:
1. Take the starting pixel.
2. Change its color to the new color.
3. Do the same for any 4-directionally connected pixels that have the same
color as the starting pixel originally had.

Return the modified image.

EXAMPLE:
Input:
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1, sc = 1, newColor = 2

Output: 
[[2,2,2],
 [2,2,0],
 [2,0,1]]
'''
# this function will scan the cell coordinate for valid colors
def pixel_scanner(grid : list[list[str]], sr : int, sc : int, new_color : str) -> list[list[str]]:
    
    if not grid:
        return 'Grid is empty.'
    
    rows, cols = len(grid), len(grid[0])

    original_color = grid[sr][sc]

    if original_color == new_color:
        return f'This is already {new_color}'
    
    color_filler(grid, sr, sc, rows, cols, original_color, new_color)
        
    return grid
    

# this function will fill up the current cell and all its neighbors 
def color_filler(grid, sr, sc, rows, cols, original_color, new_color):

    # out of bounds checker or same color
    if not(0 <= sr < rows and 0 <= sc < cols) or grid[sr][sc] != original_color:
        return
    
    grid[sr][sc] = new_color

    # DOWN
    color_filler(grid, sr + 1, sc, rows, cols, original_color, new_color)
    # UP
    color_filler(grid, sr - 1, sc, rows, cols, original_color, new_color)
    # RIGHT
    color_filler(grid, sr, sc + 1, rows, cols, original_color, new_color)
    # LEFT
    color_filler(grid, sr, sc - 1, rows, cols, original_color, new_color)

# TEST
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
# print(pixel_scanner(image, 0, 0, 2)) 
# Expected Output: 
# [[2,2,2],
#  [2,2,0],
#  [2,0,1]]
    
# SENIOR APPROACH (BY GEMINI)

def floodFill(self, image: list[list[str]], sr: int, sc: int, color: int) -> list[list[str]]:
    # 1. Capture basic data
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    
    # 2. Edge Case: If colors are the same, do nothing
    if original_color == color:
        return image
    
    # 3. Define Helper INSIDE (Closure)
    def fill(r, c):
        # Base Case: Bounds check OR wrong color
        if not (0 <= r < rows and 0 <= c < cols) or image[r][c] != original_color:
            return
        
        # Action: Paint
        image[r][c] = color
        
        # Recurse
        fill(r+1, c)
        fill(r-1, c)
        fill(r, c+1)
        fill(r, c-1)
    
    # 4. Trigger the recursion
    fill(sr, sc)
    return image

# FIND THE TOWN JUDGE
'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [a, b] represents that the person labeled a trusts the person labeled b.

Your Task: Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

EXAMPLE 1:
Input: n = 2, trust = [[1,2]]
Output: 2

EXAMPLE 2:
Input: n = 3, trust = [[1,3], [2,3]]
Output: 3

EXAMPLE 3:
Input: n = 3, trust = [[1,3], [2,3], [3,1]]
Output: -1
(Here, person 3 trusts person 1, so person 3 cannot be the judge because the judge trusts nobody.)
'''

def find_the_judge(n : int, trust : list[list[int]]) -> int:
    # prefilled lists
    # n + 1 because n is the number of people, so we need 1 more index
    # if n = 3, we have 3 people but the list indexes would be 0, 1, 2
    # if n + 1 is used, the list will have 4 indexes and we can ignore [0]
    trusts_given = [0] * (n + 1)
    trusted_by = [0] * (n + 1)

    # for trustee and trusted person in trust
    for a, b in trust:
        # get the person and GIVE one vote of trust in the
        # relative index, if a = 2 -> [0, 0, 1, 0]
        trusts_given[a] += 1
        # get the person and RECEIVE one vote of trust in the
        # respective index if b = 3 -> [0, 0, 0, 1]
        trusted_by[b] += 1
    print(f'trusts given {trusts_given}')
    print(f'trusted by {trusted_by}')

    # n + 1 in range to match the indexes of trusted_by
    for i in range(1, n + 1):
        # the judge receives votes of everyone except himself
        # so if n = 3, the judge MUST have 2 votes, that's why n - 1
        # it also cannot vote for anyone since it is the judge!
        if trusted_by[i] == n - 1 and trusts_given[i] == 0:
            return i
    # no judges found
    return -1
            
# TESTS
# trust = [[1,2]] # if n = 2 -> 2
# trust = [[1,3], [2,3]] # if n = 3 -> 3
# trust = [[1,3], [2,3], [3,1]] # if n = 3 -> -1
# print(find_the_judge(3, trust))

# SENIOR APPROACH (By Gemini):
def find_judge(n: int, trust: list[list[int]]) -> int:
    # if there's only 1 person, he's obviously the judge
    if n == 1 and not trust:
        return 1
    
    # single array to track the votes
    trust_scores = [0] * (n + 1)

    for trusting, trusted in trust:
        # the person gives a vote TO someone
        trust_scores[trusting] -= 1
        # the person receives a vote FROM someone
        trust_scores[trusted] += 1
    print(f'trust scores: {trust_scores}')

    # checks if the person has the 'perfect score' (n - 1)
    # so if n = 3, trust_scores[i] == 2 -> True
    # because the judge cannot vote for himself
    for i in range(1, n + 1):
        if trust_scores[i] == n - 1:
            return i
    # otherwise, there's no judge
    return -1

# TESTS
# trust = [[1,2]] # if n = 2 -> 2
# trust = [[1,3], [2,3]] # if n = 3 -> 3
# trust = [[1,3], [2,3], [3,1]] # if n = 3 -> -1
# print(find_judge(3, trust))