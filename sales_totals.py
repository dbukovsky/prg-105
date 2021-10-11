def main():
    sales_totals_in = open("sales_totals.txt", "r")
    totals = sales_totals_in.readlines()
    total = 0
    count = 0
    print(totals)
    for line in totals:
        line = float(line.rstrip("\n"))
        total += line
        count += 1
        print(format(line, ",.2f"))
    print("The total is:  " + format(total, ",.2f"))
    print("The number of records is: " + str(count))
    print("The average is " + format(total/count, ",.2f"))


main()
