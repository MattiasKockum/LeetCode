class Solution(object):
    def twoSum(self, nums, target):
        numbers_in_heap = {}
        for i in range(len(nums)):
            if target - nums[i] in numbers_in_heap:
                return [numbers_in_heap[target - nums[i]], i]
            numbers_in_heap[nums[i]] = i
        return []
