class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        diffLength = len(s2) - len(s1)
        s1_sorted = sorted(s1)
        for i in range(diffLength + 1):
            currentString = s2[i:i+len(s1)]
            if sorted(currentString) == s1_sorted:
                return True
        
        return False