import random

def game():
    choices = ["камень", "ножницы", "бумага", "ящер", "спок"]

    computer_choice = random.choice(choices)

    print("Choose your option:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    player_choice_index = int(input()) - 1
    player_choice = choices[player_choice_index]

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
        return 0
    elif (
        (player_choice == "камень" and (computer_choice == "ножницыs" or computer_choice == "ящер")) or
        (player_choice == "ножницыs" and (computer_choice == "бумага" or computer_choice == "ящер")) or
        (player_choice == "бумага" and (computer_choice == "камень" or computer_choice == "спок")) or
        (player_choice == "ящер" and (computer_choice == "бумага" or computer_choice == "спок")) or
        (player_choice == "спок" and (computer_choice == "камень" or computer_choice == "ножницыs"))
    ):
        print("Ты выиграл!")
        return 1
    else:
        print("Ты проиграл!")
        return -1

score = 0
question = "да"
while question.lower() == "да":
    result = game()
    score += result
    print(f"Твой счёт: {score}")
    question = input("Хотите сыграть снова? (да/нет): ")

print("Спасибо за игру! Ваш финальный счёт:", score)