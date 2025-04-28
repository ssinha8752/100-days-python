def item_in_common(l1,l2):
    dict={}
    for i in l1:
        dict[i]=True
    for j in l2:
        if j in dict:
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""