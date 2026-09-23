class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in ht:
                return [ht[diff], i]
            else:
                ht[n] = i