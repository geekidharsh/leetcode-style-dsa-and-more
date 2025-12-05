# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.


chars = ["a","a","b","b","c","c","c"]
# output = ["a","2","b","2","c","3"]

def string_compr(chars):
    res = []
    i = 0
    
    while i < len(chars):
        
        
        
        

        # if chars[right] == chars[left]:
        #     res += chars[left]
        #     count += 1
            
        # res += str(counter)
        # counter = 1