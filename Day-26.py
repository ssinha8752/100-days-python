import random

number=range(1,5)

names = ["Aasf","Badvsasdv","Cdasv","Dqwd","Eas"]

new = [i*2 for i in number]
new_names =[name.upper() for name in names if len(name)>=5]

score={name:random.randint(1,100) for name in names}
score_passed={name:sc for (name,sc) in score.items() if sc>50}

print(score_passed)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {i:len(i) for i in sentence.split()}

print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {d:(t* 9/5) + 32 for (d,t) in weather_c.items()}

print(weather_f)