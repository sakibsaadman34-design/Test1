secretnumber = 28

attempt = 0

hearts = 3

while attempt <= 3:
    Guess = int(input("Try to guess the secret number: "))
    if Guess == 28:
        print("Congratulations, you have guessed the number.")
        break
    elif Guess > 30:
        print("Keep trying")
        print("hint: less than 30")
    elif Guess <= 30:
        print("Keep trying")
    elif Guess == 29:
        print("You are close. It is less than 29")
    elif Guess <= 10:
        print("Keep Trying")
        print("Its higher than 10") 

    elif Guess <= 27:
        print("Not Correct.")
        print("Hint: It is higher than 20")

    else:
        print("Invalid Number. Please try again with a positive number")
    for i in range(1):
        attempt += 1
        print(f"You have {hearts} hearts left")
        hearts -= 1
        