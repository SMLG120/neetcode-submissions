class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob2, rob1)
            rob2 = rob1
            rob1 = temp
        return rob1

        """
        given nums = [1,2,3,1]
        iteration 1:
        temp = max(1 + 0, 0) = 1, rob2 = 0, rob1 = 1

        iteration 2:
        temp = max(2 + 0, 1) = 2, rob2 = 1, rob1 = 2

        iteration 3:
        temp = max(3 + 1, 2) = 4, rob2 = 1, rob1 = 4

        iteration 4:
        temp = max(1 + 1, 4) = 4, rob2 = 4, rob1 = 4

        return rob1 = 4
        """