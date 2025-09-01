class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the string and place each character in the appropriate row
        for char in s:
            rows[current_row] += char
            
            # Change direction when we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row
            current_row += 1 if going_down else -1
        
        # Join all rows to get the final result
        return ''.join(rows)


# test = Solution()
# print(test.convert("PAYPALISHIRING", 3))