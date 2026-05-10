class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i != j
        # smaller index first
        hashMap = {}
        res = [] # arr of indices
        for i in range(len(nums)):
            if target-nums[i] in hashMap:
                res.append(hashMap[target-nums[i]])
                res.append(i)
                return res
            hashMap[nums[i]] = i



