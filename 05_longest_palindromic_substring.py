class Solution(object):
    def longestPalindrome(self, s):
        
        start = 0
        max_length = 1
        
        # Helper function to expand around center
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        # Check each position as a potential center
        for i in range(len(s)):
            # Check odd-length palindromes (single character center)
            len1 = expand_around_center(i, i)
            # Check even-length palindromes (two character center)
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length from both cases
            curr_max = max(len1, len2)
            
            # Update if we found a longer palindrome
            if curr_max > max_length:
                max_length = curr_max
                start = i - (curr_max - 1) // 2
        
        return s[start:start + max_length]

# test = Solution()
# print(test.longestPalindrome("babad"))
