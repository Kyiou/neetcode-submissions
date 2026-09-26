class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict({nums[i]: i for i in range(len(nums))})
        result = []

        for i in range(len(nums)):
            rest = target - nums[i]

            if rest in nums_dict and nums_dict[rest] != i:
                result = [i, nums_dict[rest]]
                return result
            else:
                continue
        return result