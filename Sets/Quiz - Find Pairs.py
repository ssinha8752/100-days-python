def find_pairs(l1,l2,t):
    final=[]
    for i in l1:
        if t-i in l2:
            final.append((i,t-i))
    return final



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""