
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)
#O(n+n)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)


print_items(10)
# O(n*n)

#considering both of the above would be O(n*n + 2n)
#but since the n*n is more dominant, it would be n*n



def add_items(n):
    return n+n

# this would refer to the O(1) or it will always remain constant as the number of operations also increases


#usually the log algo will help us to keep dividing the list into 2 parts then finding the other value

# there is also nlog n which is being used in merge and quick sort to find one single value in the list of numbers

#n*n>nlogn>n>logn>k

#appening and removing from the end of the list is O(1)
#adding and removing from anywhere else in the list is O(1) as there will be a change in the indexes of all the other items present in the list









