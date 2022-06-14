i = 1
Guess = int(input("Guess: "))

while i<= 3:
    if Guess == 9:
        print("You Win!")
        break
    elif  i<3:
        Guess = int(input("Guess: "))
    else:
        print("Sorry You failed!")
    i+=1