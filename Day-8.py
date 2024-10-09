def life_in_weeks(age):
    life_remaining=(90-age)*52
    print(f"You have {life_remaining} weeks left")

life_in_weeks(56)


def calculate_love_score(name1, name2):
    word1 = 'true'
    word2 = 'love'
    count1 = 0
    count2 = 0
    for i in word1:
        f1 = name1.lower().count(i)
        print(f1)
        count1+=f1
        f2 = name2.lower().count(i)
        count1+=f2
    for i in word2:
        f3 = name1.lower().count(i)
        count2 += f3
        f4 = name2.lower().count(i)
        count2 += f4
    print(count1, count2)


calculate_love_score(name1="Angela Yu",name2 = "Jack Bauer")