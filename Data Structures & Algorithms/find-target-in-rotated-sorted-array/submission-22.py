class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]: # la partie à gauche de mid est triée
                if nums[left] <= target < nums[mid]: # target dans la partie trié
                    right = mid - 1
                else:
                    left = mid + 1
            else:# la partie à droite de mid est triée
                if nums[mid] < target <= nums[right]: # target dans partie triée
                    left = mid +1
                else:
                    right = mid-1
        
        return -1


