class Solution(object):
    def isValidSector(self, board, rows, cols):
        rows_len = len(rows)
        cols_len = len(cols)

        values = set()
        for row in range(rows_len):
            for col in range(cols_len):
                value = board[rows[row]][cols[col]]
                if value == '.':
                    continue
                if value in values:
                    return False
                values.add(value)

        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # validate rows
        for row in board:
            values = set()
            for value in row:
                if value == '.':
                    continue
                if value in values:
                    return False
                values.add(value)

        # validate columns
        for col in range(9):
            values = set()
            for row in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                if value in values:
                    return False
                values.add(value)

        rows = [0,1,2]
        cols = [0,1,2]

        while rows[2] < 9:
            while cols[2] < 9:
                if not self.isValidSector(board, rows, cols):
                    return False
                for col in range(3):
                    cols[col] += 3
            cols = [0,1,2]
            for row in range(3):
                rows[row] += 3

        return True


solution = Solution()

board = [
     ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]

board2 = [[".",".","4",".",".",".","6","3","."],
          [".",".",".",".",".",".",".",".","."],
          ["5",".",".",".",".",".",".","9","."],
          [".",".",".","5","6",".",".",".","."],
          ["4",".","3",".",".",".",".",".","1"],
          [".",".",".","7",".",".",".",".","."],
          [".",".",".","5",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."]]

print(solution.isValidSudoku(board))
print(solution.isValidSudoku(board2))