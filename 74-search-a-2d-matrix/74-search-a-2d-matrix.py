class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = 0
        col = len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False

#         rows = len(matrix)
#         cols = len(matrix[0])
#         # print(rows, cols)
        
#         start = 0
#         end = (rows*cols)-1
#         # print(left, right)
        
#         contains = False
#         while start <= end:
#             mid = (start + end) // 2
#             # mid = start + (end - start) // 2
            
#             print(mid)
#             break
        
'''
[
[1, 3, 5, 7],
[10,11,16,20],
[23,30,34,60]
]

rows, cols
  3    4 
  
left  right
0     11

'''
        
#         row = 0
#         col = len(matrix)-1
#         contains = False
        
#         while row <= len(matrix) and col >= 0:
#             if matrix[row][col] > target:
#                 col -= 1
#             elif matrix[row][col] < target:
#                 row += 1
#             else:
#                 contains = True
#         return contains
        
        
'''
- var for far right corner 
- start var

- loop while start & end vars exist
    - if end curr < target:
        - cols -=1
    - elif curr > target:
        - rows += 1
    else:
        return start, end
- -1, -1
'''