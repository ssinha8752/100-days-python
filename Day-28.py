num1=11
num2=11

print(id(num1))
print(id(num2))

num2=22
print(id(num2))

dict1={
    'value':11
}

dict2=dict1

print(id(dict1))
print(id(dict2))

dict2['value']=22

print(id(dict1))
print(id(dict2))
