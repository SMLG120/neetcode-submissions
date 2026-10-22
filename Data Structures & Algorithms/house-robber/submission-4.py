class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob2, rob1)
            rob2 = rob1
            rob1 = temp
        return rob1

        """
        given nums = [2,9,8,3,6]
        iteration 1:
        temp = max(2 + 0, 0) = 2, rob2 = 0, rob1 = 2

        iteration 2:
        temp = max(9 + 0, 2) = 9, rob2 = 2, rob1 = 9

        iteration 3:
        temp = max(8 + 2, 9) = 10, rob2 = 9, rob1 = 10

        iteration 4:
        temp = max(3 + 9, 10) = 12, rob2 = 10, rob1 = 12

        iteration 5:
        temp = max(6 + 10, 12) = 16, rob2 = 12, rob1 = 16

        return rob1 = 16
        """