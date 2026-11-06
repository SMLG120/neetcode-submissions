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

        result = [""]

        for digit in digits:
            combinations = []
            for word in result:
                for char in mapPhone[digit]:
                    combinations.append(word + char)
            result = combinations
        return result