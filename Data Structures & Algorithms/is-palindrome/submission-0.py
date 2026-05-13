class Solution:
    def isPalindrome(self, s: str) -> bool:
        despaced = ""
        for char in s:
            if not char.isalnum(): continue
            despaced += char
        
        despaced = despaced.lower()
        despaced_reverse = despaced[::-1]
        
        for i in range(len(despaced)):
            if despaced[i] != despaced_reverse[i]: return False
        
        return True
