"""
meta / facebook de / stratascratch
Find common words in any given two sentences and return them sorted alphabetically.

Constraints
    The input variables sentence1 and sentence2 must be of type str.
    The input sentences should not be empty.
    The sentences can contain any characters, including letters, numbers, punctuation marks, and whitespace.
    The sentences can be of any length, from empty strings to very long sentences.
    The sentences are case-insensitive, meaning that the comparison of words should be done in a case-insensitive manner.
    The sentences can contain duplicate words, but the output set should only contain unique common words.

Input: ["Today is a great day to learn something new!", "Is today the day to learn?"]
Output: ["day", "is", "learn", "to", "today"]
Description: This test checks if the function can correctly identify common words r
egardless of their position in the sentence and handle a simple punctuation mark.

"""

# approach: 
    # logic is doable but tricky
    # revise
import string
def find_common_words(input):
    """ 
    :type input: List[str] 
    :type sentence2: str 
    :rtype: Set[str]
    """

    sentence1 = input[0]
    sentence2 = input[1]
    
    def helper_word_cleanup(sentences):
        words = sentences.split()
        for i in range(len(words)):
            word = words[i]
            # for each word, strip the punctuation and then lower case it
            words[i] = word.strip(string.punctuation).lower()
        return words
    
    s1_set = set(helper_word_cleanup(sentence1))
    s2_set = set(helper_word_cleanup(sentence2))
    common_words = s1_set & s2_set

    return sorted(common_words)
