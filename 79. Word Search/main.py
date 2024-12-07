from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    checked = set() # (r,c) tuple
    ROWS, COLS = len(board), len(board[0])
    def search(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in checked or word[i] != board[r][c]:
            return False 

        checked.add((r, c))
        
        res = ( 
            search(r+1, c, i+1) or
            search(r-1, c, i+1) or
            search(r, c+1, i+1) or
            search(r, c-1, i+1)
        )

        checked.remove((r,c))

        return res

    for r in range(ROWS):
        for c in range(COLS):
            if search(r,c,0):
                return True

    return False 



if __name__ == "__main__":
    board = [
      ["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]
    ]

    word = "CAT"

    ans = exist(board, word)
    print(ans) # Should return true

    board = [
      ["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]
    ]

    word = "BAT"
    ans = exist(board, word)
    print(ans) # Should return true
