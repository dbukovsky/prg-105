def main():
    # get number
    num = int(input("Please enter a whole number between 20 and 100, inclusive:  "))
    good_number = validate(num)
    num_two = two(good_number)
    num_three = three(good_number)
    num_five = five(good_number)
    output = num_two + "\n" + num_three + "\n" + num_five
    printout(output)


def validate(number):
    while number < 20 or number > 100:
        print("That is not a valid")
        number = int(input("Please enter a whole number between 20 and 100, inclusive:  "))
    return number

def two(num):
    if num % 2 == 0:
        return str(num) + " is divisible by two."
    else:
        return str(num) + " is not divisible by two."


def three(num):
    if num % 3 == 0:
        return str(num) + " is divisible by three."
    else:
        return str(num) + " is not divisible by three."


def five(num):
    if num % 5 == 0:
        return str(num) + " is divisible by five."
    else:
        return str(num) + " is not divisible by five."



def printout(out):
    print(out)


main()
