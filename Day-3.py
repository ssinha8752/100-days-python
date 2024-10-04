#conditional operator
n=int(input("Number?"))
if n%2==0:
    print ('even')
else:
    print ('odd')

#PIzza order
print("Welcome to Pizza Deliveries!")
size=input("Size?")
pepperoni=input("Pepperoni?")
extra_cheese=input("Extra cheese?")

cost=0

if size=="S":
    cost+=15
    if pepperoni == "Y":
        cost += 2
elif size=="M":
    cost+=20
    if pepperoni == "Y":
        cost += 3
elif size=="L":
    cost+=25
    if pepperoni == "Y":
        cost += 3
else:
    print("Wrong choice")

if extra_cheese=="Y":
    cost+=1

print(cost)

