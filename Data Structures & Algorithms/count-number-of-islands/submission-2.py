class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0


        def isWB(r: int, c: int) -> bool:
            if (r>=0 and r<len(grid)) and (c>=0 and c<len(grid[0])):
                return True
            else:
                return False


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