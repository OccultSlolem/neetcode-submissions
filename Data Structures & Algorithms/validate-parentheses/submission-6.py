class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False

        def isProperClose(opening: str, closing: str) -> bool:
            if opening == "(" and closing == ")": return True
            elif opening == "{" and closing =="}": return True
            elif opening == "[" and closing == "]": return True
            return False

        stack = []
        opening_chars = ["(", "{", "["]
        closing_chars = [")", "}", "]"]\

        for char in s:
            if char in opening_chars:
                stack.append(char)
            elif char in closing_chars:
                if len(stack) == 0 or not isProperClose(stack[-1], char): return False
                stack.pop()
        
        return len(stack) == 0
