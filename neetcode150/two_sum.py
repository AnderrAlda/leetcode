class Solution(objet):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
