class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        r, c= len(grid), len(grid[0])

        rowSum=[list(accumulate(row, initial=0)) for row in grid]
        # use tranpose matrix trick
        colSum=[list(accumulate(col, initial=0)) for col in zip(*grid)]

        diag, antidiag=([[0]*(c+1) for _ in range(r+1)] for _ in range(2))

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                diag[i+1][j+1]=diag[i][j]+x
                antidiag[i+1][j]=antidiag[i][j+1]+x

        def isMagic(k):
            for i in range(r-k+1):
                for j in range(c-k+1):
                    Sum=diag[i+k][j+k]-diag[i][j]
                    antiD=antidiag[i+k][j]-antidiag[i][j+k]
                    match=(Sum==antiD)

                    for m in range(k):
                        if not match: break
                        match=(
                            Sum==rowSum[i+m][j+k]-rowSum[i+m][j]
                            and Sum==colSum[j+m][i+k]-colSum[j+m][i]
                        )

                    if match:
                        return True
            return False

        for k in range(min(r, c), 1, -1):
            if isMagic(k): return k
        return 1

       
