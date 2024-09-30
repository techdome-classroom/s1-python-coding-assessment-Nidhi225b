def num_islands(grid):
    # Get the dimensions of the grid
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    # Directions to explore: right, down, left, up (horizontal and vertical neighbors)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # DFS function to explore the island and mark all connected 'L' cells
    def dfs(r, c):
        # Stack for the DFS
        stack = [(r, c)]
        visited[r][c] = True
        
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 'L':
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    island_count = 0

    # Traverse every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Start a DFS when we find an unvisited 'L'
            if grid[r][c] == 'L' and not visited[r][c]:
                dfs(r, c)
                island_count += 1  # Increment the island count

    return island_count

# Input function
def input_map():
    # Take grid input from the user
    rows = int(input("Enter the number of rows: "))
    grid = []
    print("Enter the map (L for land, W for water): ")
    for _ in range(rows):
        grid.append(list(input().strip()))
    return grid

# Main function
grid = input_map()
print("Number of distinct islands:", num_islands(grid))


                    
      
