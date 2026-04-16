class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[-1]
        arr = []
        for i in range(n+1):
            arr.append(i)
        print(arr)
        if len(arr) == len(nums):
            if arr == nums:
                return n+1
        for i in range(len(arr)):
            if arr[i] in nums:
                continue
            else:
                return arr[i]