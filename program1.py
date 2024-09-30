class Solution:
    def get_total_islands(self, grid: list[list[str]]) -> int:
        num_islands = 0
        visited = [[False for _ in row] for row in grid]  # Initialize visited matrix

        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not visited[i][j] and grid[i][j] == "L":
                visited[i][j] = True
                dfs(i + 1, j)  # Explore right neighbor
                dfs(i - 1, j)  # Explore left neighbor
                dfs(i, j + 1)  # Explore bottom neighbor
                dfs(i, j - 1)  # Explore top neighbor

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "L":
                    num_islands += 1
                    dfs(i, j)  # Found a new island, explore it

        return num_islands


    


                    
      
