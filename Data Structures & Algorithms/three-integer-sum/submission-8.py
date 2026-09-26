class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            popped = sorted_nums[i]

            if popped > 0: # every other numbers are positive (since sorted)
                break
            
            if i>0 and popped == sorted_nums[i-1]:
                continue # avoid duplicate as it was already seen
            
            j, k = i+1, len(sorted_nums)-1 
            while j<k:
                twoSum = sorted_nums[j] + sorted_nums[k]
                if twoSum < -popped:
                    j+=1
                elif twoSum > -popped:
                    k-=1
                elif j<k and twoSum == -popped:
                    output.append([popped, sorted_nums[j], sorted_nums[k]])
                
                    j, k = j+1, k-1

                    while j<k and sorted_nums[j] == sorted_nums[j-1]:
                        j+=1
                
        return output