class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        dic = {}
        for value in nums:
            if value not in dic:
                dic[value] = 1
            else:
                dic[value] += 1
        max_value = nums[-1]
        min_value = nums[0]
        i = 1
        j = 0
        triplets = []
        while i != len(nums) - 1:
            target = - nums[i] - nums[j]
            if target in dic and target >= nums[i]:
                new_triplet = [nums[j], nums[i], target]
                while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                    i += 1  # Skiping duplicates
                    j = i - 1
                if new_triplet not in triplets and new_triplet.count(target) <= dic[target]:
                    triplets.append(new_triplet)
                if j == 0:
                    i += 1
                    j = i - 1
                else:
                    j -= 1
            elif max_value < target or target < min_value:
                i += 1
                j = i - 1
            else:
                j -= 1

        return sorted(triplets)
