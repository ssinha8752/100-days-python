def addTwoNumbers(l1, l2):
        print(l1,l2)
        a=l1[::-1]
        b=l2[::-1]
        n1="".join(map(str,a))
        n2 = "".join(map(str, b))
        return int(n1)+int(n2)

print(addTwoNumbers([2,4,3],[5,6,4]))