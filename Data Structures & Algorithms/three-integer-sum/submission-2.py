class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            sorted_nums = sorted(nums)
            popped = sorted_nums.pop(i)
            
            j, k = 0, len(sorted_nums)-1 
            while j<k:
                while j<k and sorted_nums[j] + sorted_nums[k] < -popped:
                    j+=1
                while j<k and sorted_nums[j] + sorted_nums[k] > -popped:
                    k-=1
                if j<k and sorted_nums[j] + sorted_nums[k] == -popped and sorted([popped, sorted_nums[j], sorted_nums[k]]) not in output:
                    output.append(sorted([popped, sorted_nums[j], sorted_nums[k]])) 
                
                j, k = j+1, k-1
                
        return output