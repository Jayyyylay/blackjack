import random
from art import logo
print(logo)
def random_number():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    num = random.choice(cards)
    return num


def condition(user_deck_total,comp_deck_total,choice):
    if user_deck_total > 21 and comp_deck_total < 21:
        print("You went over. You lose 😤")
        return False
    elif user_deck_total < 21 and comp_deck_total > 21:
        print("Opponent went over. You win 😁")
        return False
    elif user_deck_total > 21 and comp_deck_total > 21:
        print("You went over. You lose 😤")
    elif user_deck_total == 21:
        print("Win with a Blackjack 😎")
        return False
    elif comp_deck_total == 21:
        print("Lose, opponent has Blackjack 😱")
        return False
    elif choice == "no" and user_deck_total > comp_deck_total:
        print("\nYou win 😃")
        return False
    elif choice == "no" and user_deck_total < comp_deck_total:
        print("\nyou lose")
        return False
    elif choice == "no" and user_deck_total == comp_deck_total:
        ("\nITS A DRAW")
        return False

    else:
        return True
def main():
    user_deck_total = 0
    user_deck = []
    comp_deck_total = 0
    comp_deck = []
    b = 0
    while b < 2:
        user_card = random_number()
        user_deck.append(user_card)
        user_deck_total += user_card
        comp_card = random_number()
        comp_deck.append(comp_card)
        comp_deck_total += comp_card
        b += 1
    print(f"\nYour cards are {user_deck} and total is {user_deck_total}")
    print(f"Computer card is {comp_deck[0]} ")
    b = True
    while b:
        choice = input("\nDo you want to draw a card? Yes or No: ").lower()
        if comp_deck_total < 21:
            if choice != "yes" and choice != "no":
                print("Yes or No only please!")
            elif choice == "yes":
                user_deck.append(user_card)
                user_deck_total += user_card
                comp_deck.append(comp_card)
                comp_deck_total += comp_card
                print(f"your card is {user_deck} and total is {user_deck_total}")
                print(f"comp card is {comp_deck[0]}\n")
                b = condition(user_deck_total,comp_deck_total,choice)
            else:
                b = condition(user_deck_total,comp_deck_total,choice)
        else:
            b = condition(user_deck_total, comp_deck_total, choice)

    print(f"\nYour final card is {user_deck} and total is {user_deck_total}")
    print(f"Computer final card is {comp_deck} and a total of {comp_deck_total}")

def try_again():
    again = True
    while again:
        a_try = input("\nDo you want to try again? Yes or No: ").lower()
        if a_try != "yes" and a_try != "no":
            print("Please Try Again!")
        elif a_try == "yes":
            main()
        else:
            again = False

def start():
    again = True
    while again:
        print("\nWELCOME PLAYER TO THE GAME OF BLACKJACK!")
        start = input("\nPlease hit ENTER to start BlackJack or press n to exit: ").lower()
        if start != "" and start != "n":
            print("Please Try Again!")
        elif start == "":
            main()
            try_again()
        else:
            again = False


start()



