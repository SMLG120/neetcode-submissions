class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0
        while one:
            # in bound
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            # out of bounds, so append 1
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]