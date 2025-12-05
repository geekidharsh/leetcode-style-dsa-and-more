# reverse words

def reverse_words(arr: List[str]) -> List[str]:
    # pass # your code goes here
    # works o(n), not a space efficient solution
    arr_joined = ''.join(i for i in arr)
    arr_list = arr_joined.split(' ')[::-1]    
    result = []
    for i, word in enumerate(arr_list):
        for ch in word:
            result.append(ch)
        if i < len(arr_list) - 1:
            result.append(' ')
    return result

  
# debug your code below
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print(reverse_words(arr))

def reverseWordsSO(arr):