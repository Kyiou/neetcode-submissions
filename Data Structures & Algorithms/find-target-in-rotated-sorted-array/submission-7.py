class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums: List[int], target: int) -> int:

            left, right = 0, len(nums)-1

            while left <= right:
                mid = left + (right-left)//2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    left = mid+1
                elif target < nums[mid]:
                    right = mid-1
            
            return -1
        
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid        
        
        rot = left
        print(rot)
        b_nums = nums[rot:]+nums[:rot]
        print(b_nums)
        bs = binary_search(b_nums, target)
        print(bs)

        return (rot + bs)%len(nums) if bs != -1 else -1