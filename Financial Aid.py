eligible = True
status = input("Are you currently enrolled? (y/n)")
if status == "y" or status == "Y":
    gpa = float(input("What is your GPA?  "))
    if gpa < 2:
        eligible = False

drugs = input("Do you have a conviction for a drug felony?  (y/n)  ")
if drugs == "Y" or drugs == "y":
    eligible = False

credit = int(input("How many credit hours will you register for?  "))
if credit < 6:
    eligible = False

income =int(input("What is your gross yearly income?  "))
if income >= 50000:
    eligible = False

if eligible:
    print("You are eligible for financial aid.")
else:
    print("You are not eligible for financial aid.")
