from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            temp, board[i][j] = board[i][j], "#"

            found = (dfs(i+1, j, k+1) or
                     dfs(i-1, j, k+1) or
                     dfs(i, j+1, k+1) or
                     dfs(i, j-1, k+1))

            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


# ---------------- Test in VS Code ----------------
if __name__ == "__main__":
    sol = Solution()
    
    board1 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word1 = "ABCCED"
    print("Example 1:", sol.exist(board1, word1))  # True
    
    board2 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word2 = "SEE"
    print("Example 2:", sol.exist(board2, word2))  # True
    
    board3 = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    word3 = "ABCB"
    print("Example 3:", sol.exist(board3, word3))  # False
