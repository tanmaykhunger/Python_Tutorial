secret_number = 5
guess_count = 0
guess_limit = 3
You_Win = "You Win"
print("Number should be 1 to 10")
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count = guess_count + 1
    if guess == secret_number:
        print(You_Win)
        break

else:
    print(" Sorry, You Lost")