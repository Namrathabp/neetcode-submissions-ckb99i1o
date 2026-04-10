class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        res = set()
        nums.sort()
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k+1
            j = len(nums)-1
            while i < j:
                three_sum = nums[k]+nums[i]+nums[j]
                if three_sum > 0:
                    j -= 1
                elif three_sum < 0:
                    i += 1
                else:
                    res.add(tuple([nums[i], nums[k], nums[j]]))
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
        return list(res)



        