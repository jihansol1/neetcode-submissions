class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = len(matrix), len(matrix[0])

        # binary search the rows to find the potential row

        top, bot = 0, row-1

        while top <= bot:
            curr = (top + bot) // 2
            # if target is less than curr row's first element -> reduce row
            if target < matrix[curr][0]:
                bot = curr - 1
            elif target > matrix[curr][-1]:
                top = curr + 1
            else:
                break


        # binary seach the cols to find the potential col

        curr = (top + bot) // 2
        l, r = 0, col-1

        while l <= r:
            m = (l+r) // 2
            
            if target < matrix[curr][m]:
                r = m - 1
            elif target > matrix[curr][m]:
                l = m + 1
            else:
                return True

        return False 


        