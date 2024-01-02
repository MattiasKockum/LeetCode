class Solution(object):
    def isValid(self, s):
        d = {'(': [], '[': [], '{': []}
        w = {')': '(', ']': '[', '}': '{'}
        level = 0
        for c in s:
            if c in d:
                level += 1
                d[c].append(level)
                continue
            if d[w[c]] == [] or d[w[c]][-1] != level:
                return False
            d[w[c]].pop()
            level -= 1
        return level == 0
