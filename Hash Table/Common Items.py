def item_in_common(l1,l2):
    my_dict={}
    for i in l1:
        my_dict[i]=True
    for j in l2:
        if j in my_dict:
            return True
    return False

l1=[1,2,3]
l2=[2,4,5]
print(item_in_common(l1,l2))