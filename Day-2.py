#subscripting
print("Hello"[0])

#String
print("123"+"345")

#Integers
print(123+345)

#Float
print(3.14)

#Boolean
print(True)

#typecast
print(int("123")+int("456"))

print("Number of letters in your name:"+str(len(input("Enter Name"))))


#Mathmatical operators
print(123+456)
print(7-3)
print(3*2)
print(5/3) #decimal
print(5//3) #non-decimal
print(2**3)

print(3*(3+3)/3-3)

#bmi cal
height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/(height**2)

print(bmi)
print(round(bmi,2))

#f-string does not require any change of datatype
print(f"Your score is {bmi}")
