class Solution:
    def isPalindrome(self, s: str) -> bool:
        candidate = s.lower().replace(" ","")
        i, j = 0, len(candidate)-1

        while i<j:
            print(candidate[i].isalnum(), candidate[i])
            while i<j and not candidate[i].isalnum():
                i += 1
            while i<j and not candidate[j].isalnum():
                j -= 1
            
            if candidate[i] != candidate[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
