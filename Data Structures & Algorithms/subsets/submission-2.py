class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            current_length = len(res)
            for i in range(current_length):
                new_subset = res[i] + [num]
                res.append(new_subset)
        return res