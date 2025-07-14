def swap(my_list,i1,i2):
    temp=my_list[i1]
    my_list[i1]=my_list[i2]
    my_list[i2]=temp

def pivot(my_list, p_i, e_i):
    swap_index=p_i
    for i in range(p_i+1,e_i+1):
        if my_list[i]<my_list[p_i]:
            swap_index+=1
            swap(my_list,swap_index,i)
    swap(my_list, p_i, swap_index)
    return swap_index

def quick_sort(my_list,l,r):
    if l<r:
        pivot_index = pivot(my_list, l, r)
        quick_sort(my_list, l, pivot_index - 1)
        quick_sort(my_list, pivot_index + 1, r)
    return my_list

my_list=[4,6,7,3,2,1,5]
print(quick_sort(my_list,0,len(my_list)-1))