class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            cur_len = len(res)
            for i in range(cur_len):
                subset = res[i] + [num]
                res.append(subset)
        return res