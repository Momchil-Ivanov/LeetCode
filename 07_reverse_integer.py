
class Solution(object):
    def reverse(self, x):
        x_to_str = str(x)

        if x_to_str == '0':
            return 0

        is_negative = False if x_to_str[0] != '-' else True

        reverse_x_to_str = x_to_str[::-1]
        trim_reverse_x_to_str_remove_zero = reverse_x_to_str.lstrip('0')
        trim_reverse_x_to_str_remove_minus = trim_reverse_x_to_str_remove_zero.rstrip('-')
        result = int(trim_reverse_x_to_str_remove_minus)
        if is_negative:
            result = -result
        
        if result <= 2**31 -1 and result >= -2**31:
            return result
        else:
            return 0
    

# test = Solution()
# print(test.reverse(123))
# print(test.reverse(-123))
# print(test.reverse(120))
# print(test.reverse(0))
# print(test.reverse(1534236469))
