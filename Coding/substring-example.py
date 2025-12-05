arr = 'helloworld'
sub_arr = 'ow'

# create sliding window using the size of sub_arr from main arr
def substr(arr, sub_arr):
    arr_hash = {}
    j = len(sub_arr)
    i = 0
    while j <= len(arr):
        if arr[i:j] not in arr_hash:
            arr_hash[arr[i:j]] = 1
        else:
            arr_hash[arr[i:j]] += 1
        i += 1
        j += 1
    if sub_arr in arr_hash:
        return 1
    else:
        return -1

print(substr(arr, sub_arr))

