import random
def compare(user_score,comp_score):
    if user_score==comp_score:
        return "Draw"
    elif user_score==0:
        return "Win"
    elif comp_score==0:
        return "Draw"
    elif user_score>21:
        return "Win"
    elif comp_score>21:
        return "Lose"

def play_game():
    def deal_card():
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    user = []
    comp = []
    comp_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user.append(deal_card())
        comp.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user)
        comp_score = calculate_score(comp)
        print(comp[0])
        print(user)

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal = input("Another card?")
            if deal == 'Y':
                user.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp.append(deal_card())
        comp_score = calculate_score(comp)

    print(compare(user_score, comp_score))

    print(comp)


while input("Play?") == "Y":
    play_game()
