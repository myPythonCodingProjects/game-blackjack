from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    score = sum(card_list)
    if len(card_list) == 2 and score == 21:
        return 0  # Blackjack
    elif score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return score


def compare(user_card_list, computer_card_list):
    user_score = calculate_score(user_card_list)
    computer_score = calculate_score(computer_card_list)
    if user_score == computer_score:
        print("Draw")
    elif user_score == 0:
        print("You win with Blackjack")
    elif computer_score == 0:
        print("You lose, Computer has Blackjack")
    elif user_score > 21:
        print("You went over. You lose")
    elif computer_score > 21:
        print("You win. Computer went over.")
    elif user_score > computer_score:
        print("You win")
    else:
        print("You lose")

def game():
    print(logo)
    user_cards = []
    computer_cards = []

    user_cards.append(deal_card())
    user_cards.append(deal_card())

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)
    game_on = True
    while game_on:
        user_score = calculate_score(user_cards)
        print(f"Your cards:{user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_on = False
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass:")
            if hit == 'y':
                user_cards.append(deal_card())
            else:
                game_on = False

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    compare(user_cards, computer_cards)


blackjack = True
while blackjack:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        game()
    else:
        blackjack = False

