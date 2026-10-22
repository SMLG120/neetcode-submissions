class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            breakset = set()
            for j in range(i, len(s)):
                if s[j] in breakset:
                    break
                breakset.add(s[j])
            res = max(res, len(breakset))
        return res