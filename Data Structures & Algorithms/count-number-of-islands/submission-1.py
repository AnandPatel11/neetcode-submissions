class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0


        def isWB(r:int, c:int) -> bool:
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r: int, c: int) -> None:
            grid[r][c] = "-1"
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for each in dirs:
                nextr = r + each[0]
                nextc = c + each[1]
                if (isWB(nextr, nextc)):
                    if grid[nextr][nextc] == "1":
                        dfs(nextr, nextc)



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count+=1

        return count