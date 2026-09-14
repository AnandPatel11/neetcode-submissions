class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        count = 0

        def is_within_bounds(r:int, c:int) -> bool:
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r:int, c:int) -> None:
            grid[r][c] = "-1"
            dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

            for d in dirs:
                next_r = r + d[0]
                next_c = c + d[1]
                if (is_within_bounds(next_r, next_c)):
                    if grid[next_r][next_c] == "1":
                        dfs(next_r, next_c)

    




        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count+=1
        return count