'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''

def solveNQueens(n: int) -> list[list[int]]:
    res = []
    # Constructing board
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    neg_diag = set()
    pos_diag = set()

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if (r-c) in neg_diag or (r+c) in pos_diag or c in cols:
               continue

            cols.add(c)
            neg_diag.add(r-c)
            pos_diag.add(r+c)
            board[r][c] = "Q"
            backtrack(r+1)

            cols.remove(c)
            neg_diag.remove(r-c)
            pos_diag.remove(r+c)
            board[r][c] = "."


    backtrack(0)
    return res




if __name__ == "__main__":
    res = solveNQueens(4)
    print(res)
