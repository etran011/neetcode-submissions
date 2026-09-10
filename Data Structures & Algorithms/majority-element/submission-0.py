from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = defaultdict(int)
        maj = len(nums)/2

        for n in nums:
            table[n] += 1

            if table[n] > maj:
                return n