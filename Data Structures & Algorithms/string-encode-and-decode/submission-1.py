class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        convert each char to its ascii representation using ord()
        between each word, add a pipe |
        between each entry, insert an asterisk
        at the end, insert a pound sign
        """

        def encode_word(word: str) -> str:
            output_str = ""
            for char in word:
                output_str += str(ord(char))
                output_str += "|"
            return output_str
        
        encoded = ""
        for i in range(len(strs)):
            word = strs[i]
            encoded += encode_word(word)
            is_last_index = i == (len(strs) - 1)
            if is_last_index: encoded += "#"
            else: encoded += "*"
        return encoded


    def decode(self, s: str) -> List[str]:
        if s == "#": return [""]
        def decode_word(word: str) -> str:
            output_str = ""
            decode_buffer = ""

            for char in word:
                if char == "|":
                    output_str += chr(int(decode_buffer))
                    decode_buffer = ""
                else:
                    decode_buffer += str(char)

            return output_str
        
        decoded_words: List[str] = []
        decode_buffer = ""
        for char in s:
            if char == "*":
                decoded_words.append(decode_word(decode_buffer))
                decode_buffer = ""
                continue
            elif char == "#":
                decoded_words.append(decode_word(decode_buffer))
                return decoded_words
            decode_buffer += char
        return []

