# given a string sentence that consist of words separated by spaces
# convert the sentence to "Goat Latin" 
# If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
# For example, the word "apple" becomes "applema".
# If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

def toGoat(sentence):
    to_goat = []
    words = sentence.split(' ')
    vowels = 'aeiou'

    for idx, word in enumerate(words):
        # lower() to make sure all vowels are compared in lower case
        if word[0].lower() in vowels:
            new_word = word+'ma'
        else:
            new_word = word[1:] + word[0] + 'ma'
        # add 'a' based on index
        new_word += 'a' * (idx + 1)
        to_goat.append(new_word)
    
    return ' '.join(i for i in to_goat)

sentence = "I speak Goat Latin"
toGoat(sentence)