class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if sorted(set(nums)) == nums:
            return False
        else:
            return True