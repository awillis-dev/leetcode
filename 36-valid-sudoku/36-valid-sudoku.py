class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]  # validate row
        cols = [set() for _ in range(9)]  # validate col
        boxes = [set() for _ in range(9)] # validate square :: key => (row//3, col//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                box = (r // 3) * 3 + c // 3
                if val in boxes[box]:
                    return False
                boxes[box].add(val)

        return True

	# 		if board[r][c] == ".":  # if cell is empty, continue
	# 			continue
	# 		if (board[r][c] in rows[r] or  # check for duplicates in row, col, box
	# 			board[r][c] in cols[c] or
	# 			board[r][c] in boxes[r//3][c//3]:
	# 			return False
	#
	# 		cols[c].add(board[r][c])       # add current values to sets
	# 		rows[r].add(board[r][c])
	# 		boxes([(r//3, c//3)]).add(board[r][c])
	# return  True