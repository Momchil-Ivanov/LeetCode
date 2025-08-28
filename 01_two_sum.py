class Solution(object):
    def twoSum(self, nums, target):
        for first_index in range(len(nums)):
            for second_index in range(first_index + 1, len(nums)):
                if nums[first_index] + nums[second_index] == target:
                    return [first_index, second_index]


test = Solution()
print(test.twoSum([3,3], 6))
