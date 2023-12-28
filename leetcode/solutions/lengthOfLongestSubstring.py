class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substring_dict = {}
        max_len = 0
        now_len = 0
        start_pos = 0
        for pos, char in enumerate(s):
            now_len += 1
            if char not in substring_dict or substring_dict[char] < start_pos:
                if now_len > max_len:
                    max_len = now_len
            else:
                now_len = pos - substring_dict[char]
                start_pos = substring_dict[char]
            substring_dict[char] = pos
        return max_len
