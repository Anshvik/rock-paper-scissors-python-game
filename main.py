import random

print("Welcome to Rock, Paper, Scissor Game!")

game = ["rock", "paper", "scissor"]

# Initialize scores
user_score = 0
computer_score = 0
draws = 0

while True:
    try:
        user_input = input("\nChoose rock, paper, or scissor (or type 'exit' to quit): ").lower()

        if user_input == 'exit':
            print("\n🏁 Final Score:")
            print(f" You: {user_score} |  Computer: {computer_score} |  Draws: {draws}")
            print("Thanks for playing! ")
            break

        if user_input not in game:
            print(" Invalid input. Please try again.")
            continue

        secret = random.choice(game)
        print(f"Computer chose: {secret}")

        if user_input == secret:
            print(" It's a Draw!")
            draws += 1
        elif (user_input == "rock" and secret == "scissor") or \
             (user_input == "paper" and secret == "rock") or \
             (user_input == "scissor" and secret == "paper"):
            print(" You won this round!")
            user_score += 1
        else:
            print("You lost this round!")
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score} | Draws: {draws}")

    except Exception as e:
        print(" Unexpected error. Please try again.")
