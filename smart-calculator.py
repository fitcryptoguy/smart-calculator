def Addition():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    ans = num1 + num2
    print(f"Answer is {ans}".format(ans))
    while True:
        user_sub = input("""
    Do you want to add more numbers to Answer? y/n 
     r for starting over the addition:    """)

        if user_sub == "n":
            break

        elif user_sub == "y":
            try:
                a = float(input("enter another number: "))
                ans = ans + a
                print(ans)
            except:
                print("invalid input")

        elif user_sub == "r":
            Addition()

        else:
            print("Invalid input")
#################################################################################################################################
def Substraction():
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    ans = num1 - num2
    print(ans)
    while True:
        user_sub = input("""
Do you want to Substract more numbers?
Type 'y' for yes and 'n' for going back to Main Menu 
'r' for starting over the substraction :   """)
        if user_sub == "n":
            break

        elif user_sub == "y":
            a = float(input("enter another number: "))
            ans = ans - a
            print(ans)

        else:
            print("Invalid input sir. Try again  ")
####################################################################################################################################################
def Multiply():
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    ans = num1 * num2
    print(ans)
    while True:
        user_sub = input("""
    Do you want to Multiply more numbers?

    Type 'y' for yes and 'n' for going back to Main Menu  :   """)
        if user_sub == "n":
            break


        elif user_sub == "y":
            a = float(input("enter another number: "))
            ans = ans * a
            print(ans)
#############################################################################################################################################
def Devide():
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    ans = num1 / num2
    print(ans)
    while True:
        user_sub = input("""
    Do you want to add more numbers?

    Type 'y' for yes and 'n' for going back to Main Menu  :   """)
        if user_sub == "n":
            break


        elif user_sub == "y":
            a = float(input("enter another number: "))
            ans = ans / a
            print(ans)
#######################################################################################################################################

while True:
    print("")
    print("Type 'a' for Addition")
    print("Type 's' for Substraction")
    print("Type 'm' for Multipliication")
    print("Type 'd' for Devide")
    print("type 'q' for Quitting the calculator")
    print("")
    user = input("Enter Response: ")


    if user.lower() == "a":
        Addition()

    elif user.lower() == "s":
        Substraction()

    elif user.lower() == "m":
        Multiply()

    elif user.lower() == "d":
        Devide()

    elif user.lower() == "q":
        print("Thank you for using me")
        break

    else:
        print("Invalid Input, please enter again")




