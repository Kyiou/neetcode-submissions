class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_before = [nums[0]]

        for i in range(1, len(nums)):
            product_before.append(product_before[i-1]*nums[i])

        product_after = [1] * len(nums)
        product_after[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            product_after[i] = nums[i] * product_after[i+1]
        
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(product_after[i+1])
            elif i == len(nums)-1:
                result.append(product_before[i-1])
            else:
                result.append(product_before[i-1]*product_after[i+1])

        return result
         