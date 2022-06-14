# i = 1
# Guess = int(input("Guess: "))
#
# while i<= 3:
#     if Guess == 9:
#         print("You Win!")
#         break
#     elif  i<3:
#         Guess = int(input("Guess: "))
#     else:
#         print("Sorry You failed!")
#     i+=1

guess_count = 0
secret_number = 9
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print('You Win!')
        break
else: #while loop can also have else statement, if while loop completes then will go to the else loop , otherwise if the while loop is interrupted by break , then else loop will not execute
    print("Sorry You failed!")