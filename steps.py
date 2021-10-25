def main():
    total = 0
    steps_per_day = {}
    minimum = 0
    maximum = 0
    minimum_days = ""
    maximum_days = ""
    for day in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
        steps = int(input("Please enter the number of steps for " + day + ":  "))
        total += steps
        steps_per_day[day] = steps

    # max steps per day
    for date in steps_per_day:
        if steps_per_day[day] > maximum:
            maximum = steps_per_day[date]
            maximum_days = date
        elif steps_per_day[date] == maximum:
            maximum_days += ", " + date
    print(maximum_days + " had the most steps with a total of:  " + str(maximum))

    for date in steps_per_day:
        if steps_per_day[day] > minimum:
            minimum = steps_per_day[date]
            minimum_days = date
        elif steps_per_day[date] == minimum:
            minimum_days += ", " + date
    print(minimum_days + " had the least steps with a total of:  " + str(minimum))



main()
