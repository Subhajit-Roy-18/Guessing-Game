""" PROBLEM - CREATE A GAME WHICH WILL TAKE A NUMBER AS AN INPUT FROM THE USER, AND IF THAT INPUT MATCHES WITH
              THE SECRET NUMBER, THE USER WINS.
    CONDITIONS:-
    (i) No. of Attempts = 10
    (ii) The User should be Informed with the Remaining no. of Guesses.
    (iii) You also have to let the User know whether he has to Increase the Typed Number or Decrease it.
"""



print("This is a Number Guessing Game.")
print("You have to keep Entering Numbers until you Guess the Numeric Value, I have set.")
print("Oh! Let me tell you one more thing. You only have FIVE LIVES, So BE CAREFUL!! \n \n")


def clue():
    print("Hint: The number is a multiple of 3.")


def main():
    Secret = 45
    Lives = 5
    Attempts = 0

    print("Best of Luck!")
    print("Let's Start.")

    while True:
        print("\n Input your Number.")
        N = int(input())

        Lives = Lives - 1
        Attempts = Attempts + 1



        if N == Secret:
            print("Hurrah!!!")
            print("You have done it.")
            print("Congratulations!!!")

            print("\n Attempts:", Attempts)
            break

        if Lives == 0:
            print("You ran out of Lives.")
            print("Game Over!! \n")

            print("Do you want to play this again?")
            print("Type Yes if you do.")
            Again = input().capitalize()

            if Again == "Yes":
                print("\n")
                main()

            else:
                print("\n")
                print("Thanks for Playing.")
                break


        elif 55 >= N > Secret:
            print("You're very close, Try to Decrease your Number a bit.")
            print("Tries Remaining:", Lives)

        elif N > 55:
            print("Decrease your Number. You're way too far.")
            print("Tries Remaining:", Lives)

        elif 35 <= N < Secret:
            print("You're just a little away. Try to Increase your Number a bit.")
            print("Tries Remaining:", Lives)

        elif N < 35:
            print("You're not even close. Increase your Number.")
            print("Tries Remaining:", Lives)

        if Lives == 1:
            print("\n Do you want a Clue?")
            print("Type Yes or No, according to your wish.")

            Answer = input().capitalize()
            if Answer == "Yes":
                print("\n OK, here it is.")
                clue()

            elif Answer == "No":
                print("As you wish.")
                continue

            else:
                print("\n Wrong Input!!")
                continue


main()
