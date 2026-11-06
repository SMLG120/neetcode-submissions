class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapPhone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        result = []

        def backtrack(i, curString):
            if len(curString) == len(digits):
                result.append(curString)
                return
            for char in mapPhone[digits[i]]:
                backtrack(i + 1, curString + char)


        backtrack(0, "")
        
        return result