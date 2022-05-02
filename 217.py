class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}

        for n in nums:
            if(n in nums_dict.keys()):
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1
            if nums_dict[n] > 1:
                return True
        return False

