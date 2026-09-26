class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict({nums[i]: i for i in range(len(nums))})
        result = None

        for i in range(len(nums)):
            rest = target - nums[i]

            if (nums_dict.get(rest, None) is not None) & (i != nums_dict.get(rest, None)):
                result = [i, nums_dict[rest]]
                return result
            else:
                continue