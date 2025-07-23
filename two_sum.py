#class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]