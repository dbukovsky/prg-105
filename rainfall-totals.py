"""
    Import the data from the file. Check to see if the data is valid, if it is not valid,
    indicate to the user what the bad data is. Total and average the data,
    and display formatted results on the screen.
"""


def main():
    try:
        in_file = open("rainfall-totals.txt", "r")
        rain_list = in_file.readlines()
        in_file.close()
        total = 0
        count = 0

        for month in rain_list:
            rain_data = month.split()
            month = rain_data[0]
            inches = rain_data[1].rstrip("\n")
            valid = True
            for item in inches:
                if not item.isdigit() and item != ".":
                    valid = False
                if not valid:
                    print("The data for " + month + " is " + inches + ", which is not numeric")
                else:
                    total += float(inches)
                    count += 1
                    print('The total of valid entries is: ' + format(total, ",.2f"))
                    print('The average of valid entries is: ' + format(total, ",.2f"))

    except IOError:
        print("File not found")


main()
