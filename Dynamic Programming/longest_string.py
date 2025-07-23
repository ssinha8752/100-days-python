def find_longest_string(s):
    s_len=0
    ans=""
    for i in range(len(s)):
        if len(s[i])>s_len:
            s_len=len(s[i])
            ans=s[i]
    return ans

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)

"""
    EXPECTED OUTPUT:
    ----------------
    banana

"""