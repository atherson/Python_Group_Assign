import random

numbers = [2, 3, 6, 7, 10]

while True:
    try:
        rounds = int(input("Enter Number Of Rounds Between 1 and 7: "))
        if 1 <= rounds <= 7: 
            break
        else:
            print("\nInvalid input! Enter a number between 1 and 7\n".upper())
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

total_score = 0  
save_number = set()
score_history = []

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    
    while True:
        lucky_number = input("Enter a lucky number: ")
        
        if not lucky_number.isdigit():
            print("Invalid input! Please enter a number.")
            continue 

        lucky_number = int(lucky_number)

        if lucky_number in save_number:
            print("Number is already entered! Try again.")
        else:
            save_number.add(lucky_number)
            print("Number is saved and you cannot enter it again.")
            break 

    num = random.choice(numbers)
    remainder = lucky_number % num 

    print(f"Randomly chosen divisor: {num}")

    if remainder == 0:
        print("It's a draw!")
        total_score += 1
    elif remainder % 2 == 0:
        print("It's a win!")
        total_score += 3
    else:
        print("It's a loss!")
        total_score -= 3

    score_history.append(total_score)
    print(f"Total Score after Round {round_num}: {total_score}")


average_score = sum(score_history) / len(score_history)

print("\nGame Over!")
print(f"Final Total Score: {total_score}")
print(f"Average Total Score per Round: {average_score:.2f}")

if total_score > 0:
    print("Congratulations! You win! 🎉")
elif total_score < 0:
    print("You lost! Better luck next time. 😢")
else:
    print("It's a draw! 🤝")
