number=range(1,5)

names = ["Aasf","Badvsasdv","Cdasv","Dqwd","Eas"]

new = [i*2 for i in number]
new_names =[name.upper() for name in names if len(name)>=5]

print(new_names)