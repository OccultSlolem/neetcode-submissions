class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s_chars = {}
        for s_char in s:
            if s_char not in s_chars: s_chars[s_char] = 0
            s_chars[s_char] += 1
        t_chars = {}
        for t_char in t:
            if t_char not in t_chars: t_chars[t_char] = 0
            t_chars[t_char] += 1
        
        return s_chars == t_chars
        