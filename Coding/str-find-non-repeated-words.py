"""
Find non-repeated words in any given 2 sentences.

To find non-repeated words in any given two sentences, we can use the 
Counter module from the collections package. The goal is to count occurrences of each 
word in both sentences and return a list of words that appear only once.

Input: ["The cat in the hat", "A cat in a mat"]
Output: ["The", "the", "hat", "A", "a", "mat"]
Description: This tests the function’s ability to identify non-repeated words between sentences with 
slight variations and common stop words.
"""

from collections import Counter
def non_repeated_words(input):
    """
    :type input: List[str]
    :rtype: List[str]
    """
    # question wording in kinda confusing
    # job is to find all non non_repeated_words across two sentences

    sentence1 = input[0]
    sentence2 = input[1]
    
    s1_words = sentence1.split()
    s2_words = sentence2.split()
    
    all_words = s1_words + s2_words
    all_words = Counter(all_words)
    
    non_repeated_words = []
    for item, count in all_words.items():
        if count == 1:
            non_repeated_words.append(item)
    return non_repeated_words