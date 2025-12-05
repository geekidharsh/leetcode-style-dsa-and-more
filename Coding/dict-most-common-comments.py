"""
Get most frequent comment accross all comment at 
restaurants: { rest1: [list of comments], rest2: [list of comments] } 

Do not double count the comment from the same location - 
so use a set first to iterate over all the lists then turn them to a set, 
and you can then create a new dict with
data = {
    "rest1": ["great food", "friendly staff", "great food"],
    "rest2": ["friendly staff", "clean space"],
    "rest3": ["great food", "clean space", "friendly staff", "friendly staff"]
}
"""
# meta, data engineer

data = {
    "rest1": ["great food", "friendly staff", "great food"],
    "rest2": ["friendly staff", "clean space"],
    "rest3": ["great food", "clean space", "friendly staff", "friendly staff"]
}

def most_common_comments(data):
    data_set = {}
    
    for rest in data:
        # turn data and comments into dict with set of comments, this ensures uniqueness per rest
        if rest not in data_set:
            data_set[rest] = set()

        for cm in data[rest]:
            data_set[rest].add(cm)
    
    # print(data_set)
    # flatten all comments in dataset to get count
    all_comments = []
    for rest in data_set:
        cm = data_set[rest]
        all_comments.extend(list(cm))
    # print(all_comments) 
    
    import collections
    comment_count = collections.Counter(all_comments)
    # print(comment_count)
    max_count = max(comment_count.values())
    for comment in comment_count:
        if comment_count[comment] == max_count:
            return comment

most_common_comments(data)