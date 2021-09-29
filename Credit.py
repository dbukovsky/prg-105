score = int(input("What is your numeric credit score?"))
if score > 719:
    print("You have excellent credit.")
elif score > 689:
    print("You have good credit. ")
elif score > 629:
    print("You have fair credit. ")
elif score > 0:
    print("You have bad credit. ")
else:
    print("That is not a valid value. ")
