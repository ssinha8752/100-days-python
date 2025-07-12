def merge(l1,l2):
    combined=[]
    i=0
    j=0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            combined.append(l1[i])
            i+=1
        else:
            combined.append(l2[j])
            j+= 1

    while i<len(l1):
        combined.append(l1[i])
        i+=1

    while j < len(l2):
        combined.append(l2[j])
        j+=1

    return combined


def merge_sort(my_list):
    if len(my_list)==1:
        return my_list
    mid_index=int(len(my_list)/2)
    left=merge_sort(my_list[:mid_index])
    right=merge_sort(my_list[mid_index:])

    return merge(left,right)

print(merge([1,3,5,7],[2,4,6,8]))