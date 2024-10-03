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

#Final Project
print("Welcome to tip calculator")
bill=float(input("Whats the total bill?"))
tip=int(input("How much tip would you like to give? 10, 12 or 15?"))
pax=int(input("How many people to split the bill?"))
tip_percent=tip/100
total=bill+bill*tip_percent
bill_pp=total/pax
final_amount=round(bill_pp,2)
print(f"Each person should pay : S$ {final_amount}")