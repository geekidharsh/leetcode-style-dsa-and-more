"""Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. 
For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. 
For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.

You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
"""

def groupShiftStrings():
    # creating custom hashmap is important here
    # understand: 
    # shfifting diff in valid seqence (words) is consistent
    # so 2 words with same shifting diff will be interchangeable
    # convert all words in strings to its corresponding ord()

    #helper
    def get_shift_pattern(string):
        # to make keys for the hashmap, using common shifting pattern into one group
        if len(string) == 1:
            return '0'

        pattern = ''
        for i in range(1, len(string)):
            # this is the important trick
            val = (ord(string[i]) - ord(string[i-1]))%26
            pattern += str(val)
        return pattern

    string_map = defaultdict(list)
    for string in strings:
        pattern = get_shift_pattern(string)
        print(pattern)
        string_map[pattern].append(string)
    
    return list(string_map.values())
    