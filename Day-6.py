#Loops
import random

fruits=["Apple","Peach","Pear"]
for k,i in enumerate(fruits):
    print(k,i)


scores=[121,443,343,414,564,623,137,833,913,210]

max=scores[0]

for score in scores:
    if score>max:
        max=score

print(max)


#Range
sum=0
for i in range(1,101):
    sum=sum+i

print(sum)


for i in range(1,101):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(f"{i}")



#password:
print("PyPassword Generator")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special = ['!', '@', '#', '$', '%', '*']

l = int(input("How many letters? "))
s = int(input("Symbols? "))
n = int(input("Numbers? "))

selected_letters = [letters[random.randint(0, len(letters) - 1)] for i in range(l)]
selected_numbers = [numbers[random.randint(0, len(numbers) - 1)] for i in range(n)]
selected_special = [special[random.randint(0, len(special) - 1)] for i in range(s)]

password_list = selected_letters + selected_numbers + selected_special
random.shuffle(password_list)
password = ''.join(password_list)

print("Generated password:", password)



