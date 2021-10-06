"""
    Create a program that presents the user with five choices. The topic could be game characters, food, car packages,
    anything you are interested in. You will put a menu on the screen, ask the user to enter the number or letter of
    their choice, and then call the corresponding function to give the user more information. See the sample
    screen below:
"""




def main():
    # menu
    print("1. Hot Dog \n2. Burger \n3. Gyro \n4. Italian Beef \n5. Fried Chicken")
    choice = int(input("Please type the number of your selection: "))

    if choice == 1:
        one()
    elif choice == 2:
        two()
    elif choice == 3:
        three()
    elif choice == 4:
        four()
    elif choice == 5:
        five()
    else:
        print("That is not a valid choice")


def one():
    print("All beef hot dog on a steamed bun.")


def two():
    print("Beef patty on a sesame bun with your choice of cheese.")


def three():
    print("Lamb meat on a grilled pita.")


def four():
    print("Italian beef soaked in juice and spices on a french roll.")


def five():
    print("Crispy wing, thigh, breast, or leg.")


main()
