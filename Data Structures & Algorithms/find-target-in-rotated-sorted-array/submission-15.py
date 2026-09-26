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
        left_search = binary_search(nums[:rot], target)
        if left_search != -1:
            return left_search

        right_search = binary_search(nums[rot:], target)
        
        return (rot + right_search)%len(nums) if right_search != -1 else -1