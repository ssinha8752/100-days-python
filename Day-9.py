#dictionaries are key and value pairs sivided by :
p={"A":"B","C":"D"}

for k,i in enumerate(p):
    print(k,p[i])


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])





