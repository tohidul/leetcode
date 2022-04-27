class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind=0
        for i in nums:
            for j in range(ind+1,len(nums)):
                if (i + nums[j]) == target:
                    return [ind,j]
            ind+=1
                    