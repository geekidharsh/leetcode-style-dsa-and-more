"""Search Suggestions System
Design a system that suggests at most three product names from products after each character 
of searchWord is typed. Suggested products should have common prefix with searchWord. If there 
are more than three products with a common prefix return the three lexicographically minimums 
products. Return a list of lists of the suggested products after each character of searchWord is typed.

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],
         ["mobile","moneypot","monitor"],
          ["mouse","mousepad"],
          ["mouse","mousepad"],
          ["mouse","mousepad"]]
          
"""


# solution:
    # - question looks complicated: simplification is
        # for every prefix, show suggestions up to 3 of products - in sorted order
    # to solve, we first sort the products
    # then we run two iterations, one for each prefix and
    # for each prefix, checking products that match the prefix
    # break once suggestion reaches 3
    # create a list of final suggestions
    # time complexity: o(nlogn) for sorting, then m for each prefix: N*M*logM
    # space: o(n)

def search_suggested(products, searchWord):
    sorted_prod = sorted(products)
    final_suggestions = []

    for ch in range(len(searchWord)):
        prefix = searchWord[:ch + 1]
        suggestions = []
        
        for item in sorted_prod:
            if item.startswith(prefix):
                suggestions.append(item)
            if len(suggestions) > 2:
                break
        final_suggestions.append(suggestions)


    return final_suggestions
    

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
    
search_suggested(products, searchWord)