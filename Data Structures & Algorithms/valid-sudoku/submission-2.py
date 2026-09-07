class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
     
     rows=defaultdict(set) #which means for every row create a set. rows= (set() for _ in range(9)) this is the meaning
     cols=defaultdict(set)
     squares=defaultdict(set)

     for r in range(9):
        for c in range(9):
            value=board[r][c]

            if value=='.':
                continue
            if (value in rows[r] or value in cols[c] or value in squares[(r//3, c//3)]):
                return False
            rows[r].add(value)
            cols[c].add(value)
            squares[(r//3, c//3)].add(value)  
     return True
            # print(value)
        # return True