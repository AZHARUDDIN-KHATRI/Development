print("Welcome to the bank")

pin = 8786
balance = 0

userPinInput = int(input("Please enter your pin -> "))

if userPinInput == pin:
    print("Your pin has been confirmed")
    print("Choose the option ->[1] Check Balance\
    [2] Deposit Money\
    [3] Withdraw Money\
    [4] Exit")

    userInput = int(input())

    while(userInput != 4):
        if userInput == 1:
            print(balance)
        elif userInput == 2:
            val = int(input())


else:
    print("Your pin is invalid")