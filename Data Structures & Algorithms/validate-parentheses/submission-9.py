class Solution:
    def isValid(self, s: str) -> bool:
        # An odd length string can't be valid
        if len(s) % 2 != 0: return False

        stack = []
        bracketMap = {')': '(', '}': '{', ']': '['}

        for char in s:
            print(stack)
            if char in bracketMap:
                topElement = stack.pop() if stack else '#'
                if bracketMap[char] != topElement: return False
            else:
                stack.append(char)
        
        return len(stack) == 0
