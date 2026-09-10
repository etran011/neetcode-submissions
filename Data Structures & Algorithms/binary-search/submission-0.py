class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for s in range(0, len(nums)):
            if nums[s] == target:
                return s
        return -1


        