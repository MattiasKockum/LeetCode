class Solution(object):
    def maxArea(self, height):
        max_value = 0
        i = 0
        j = len(height) - 1
        max_height = max(height)

        while i < j:
            test_value = min(height[i], height[j]) * (j - i)
            max_value = max(max_value, test_value)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

            if (max_height * (j - i)) <= max_value:
                break

        return max_value
