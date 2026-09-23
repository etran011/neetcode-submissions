class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for i in range(0, len(nums)):
            if nums[i] in ht:
                return True
            else:
                ht[nums[i]] = i
        return False

        