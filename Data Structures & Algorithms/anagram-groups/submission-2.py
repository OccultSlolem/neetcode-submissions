class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict(
            # 'act': ['cat', 'tac']
        )

        for string in strs:
            alphabetized_string_chars = "".join(sorted(string))
            if alphabetized_string_chars not in anagrams:
                anagrams[alphabetized_string_chars] = [string]
            else:
                anagrams[alphabetized_string_chars].append(string)
        
        return list(anagrams.values())

