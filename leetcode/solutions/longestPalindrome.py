class Solution(object):
    def longestPalindrome(self, s):
        print(f"Input : {s=}")
        longest = s[0]
        for i in range(len(s)):
            # even
            if i + 1 < len(s) and s[i] == s[i + 1]:
                print(f"testing even at {i}")
                l = 1
                while i - l + 1 > 0 and i + l + 1 < len(s) and s[i - l] == s[i + 1 + l]:
                    l += 1
                if 2 * l > len(longest):
                    longest = s[i - l + 1: i + l + 1]
                print(longest)
            # uneven
            if i + 1 < len(s) and 0 < i and s[i - 1] == s[i + 1]:
                print(f"testing uneven at {i}")
                l = 1
                while i - l > 0 and i + 1 + l < len(s) and s[i - 1 - l] == s[i + 1 + l]:
                    l += 1
                if 2 * l + 1 > len(longest):
                    longest = s[i - l: i + l + 1]
                print(longest)
        return longest
