def first_non_repeating_char(s):
    dict={}
    final=[]
    for i in s:
        dict[i]=dict.get(i, 0) + 1

    result = "".join(str(key) for key, count in dict.items() if count == 1)
    ans=[i for i in result]
    if ans:
        return ans[0]
    else:
        return None

print( first_non_repeating_char('leetcode') )
print( first_non_repeating_char('hello') )
print( first_non_repeating_char('aabbcc') )


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""