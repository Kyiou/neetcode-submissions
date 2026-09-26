class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_consecutive = 0

        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                n_consecutive = 1
                while nums[i]+n_consecutive in nums_set:
                    n_consecutive += 1
            
                max_consecutive = max(max_consecutive, n_consecutive)

        return max_consecutive