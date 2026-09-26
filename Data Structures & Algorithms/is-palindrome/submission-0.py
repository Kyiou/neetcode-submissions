class Solution:
    def isPalindrome(self, s: str) -> bool:
        candidate=""

        for c in s:
            if c.isalnum():
                candidate += c.lower()

        return candidate == candidate[::-1]