from Roll import Roll
import random

def main():
    print_header()
    game_loop()



def print_header():
    print("-----------------------------")
    print("-----Rock-Paper-Scissors-----")
    print("-----------------------------")

def game_loop():
    player_name = input("What is your name?\n")
    print(f"Ok {player_name}, let's do this!")

    rolls = [Roll("Rock"),
             Roll("Paper"),
             Roll("Scissors")]

    count = 0
    player_counter_win = 0
    computer_counter_win = 0

    while count < 3:
        player_roll = input("\nPlease choose your roll [r]ock, [p]aper or [s]cissors: \n")
        computer_roll = random.choice(rolls)

        if player_roll == 'r':
            if computer_roll.name == "Rock":
                print(f"It's a draw the computer choose also {computer_roll.name}")
                count += 1
                continue
            elif computer_roll.name == "Paper":
                print(f"Computer won as it chose {computer_roll.name}. You Lose!")
                computer_counter_win += 1
                count += 1
                continue
            elif computer_roll.name == "Scissors":
                print(f"You won this one, as the computer chose {computer_roll.name}. Congratulations!")
                player_counter_win += 1
                count += 1
                continue
        elif player_roll == 'p':
            if computer_roll.name == "Rock":
                print(f"You won this one, as the computer chose {computer_roll.name}. Congratulations!")
                player_counter_win += 1
                count += 1
                continue
            elif computer_roll.name == "Paper":
                print(f"It's a draw the computer choose also {computer_roll.name}")
                count += 1
                continue
            elif computer_roll.name == "Scissors":
                print(f"Computer won as it chose {computer_roll.name}. You Lose!")
                computer_counter_win += 1
                count += 1
                continue
        elif player_roll == 's':
            if computer_roll.name == "Rock":
                print(f"Computer won as it chose {computer_roll.name}. You Lose!")
                computer_counter_win += 1
                count += 1
                continue
            elif computer_roll.name == "Paper":
                print(f"You won this one, as the computer chose {computer_roll.name}. Congratulations!")
                player_counter_win += 1
                count += 1
                continue
            elif computer_roll.name == "Paper":
                print(f"It's a draw the computer choose also {computer_roll.name}")
                count += 1
                continue


    if player_counter_win > computer_counter_win:
        who_won = "Player"
    else:
        who_won = "Computer"



    print()
    print(f"The ultimate winner for the whole game is the {who_won}")
    print(f"The player_counter_win: {player_counter_win} and the computer_counter_win: {computer_counter_win}")








if __name__ == '__main__':
    main()