class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        all_nums = nums1 + nums2
        all_nums.sort()
        
        n = len(all_nums)
        if n % 2 == 0:
            # Even number of elements - average of two middle elements
            median_of_all_nums = (all_nums[n//2 - 1] + all_nums[n//2]) / 2.0
        else:
            # Odd number of elements - middle element
            median_of_all_nums = all_nums[n//2]
        
        return median_of_all_nums

# Test the function
# test = Solution()
# print(test.findMedianSortedArrays([1,3], [2]))