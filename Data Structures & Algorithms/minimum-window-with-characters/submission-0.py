class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}

        # count occurence of letters in T and store in countT
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            # add char to window map
            window[c] = 1 + window.get(c, 0)

            # update map of have
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update our result
                if (r - l - 1) < resLen:
                    res = [l, r]
                    resLen = (r - l - 1)
                # pop left character
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
                            
