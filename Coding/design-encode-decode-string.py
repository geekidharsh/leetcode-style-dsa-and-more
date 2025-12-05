# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network 
# and is decoded back to the original list of strings.

# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc_str = ''

        for i in strs:
            enc_str += str(len(i))+'#'+i
            print(enc_str)
        return enc_str

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        dec_list = []
        i = 0
        while i < len(s):
            j = i
            while j != '#':
                j += 1

            length = s[i:j]          
            # word will appear after first #
            word = s[j+1:length]
            dec_list.append(word)
            i = j + length + 1
        return dec_list




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))