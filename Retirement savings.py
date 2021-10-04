year = 1
age = int(input("How old are you?"  ))
retire = int(input("What age do you want to retire?  "))
income = float(input("What is your yearly income?  "))
save = int(input("What percentage of your income do you save(whole number)?  "))
percent = save/100
savings = float(input("How much do you currently have saved?  "))
print("This projection assumes a 3% raise each year and a 6% yearly return on investment")

print("Year          Income")
years = retire - age
while year < years + 1:
    print(format(year, '4.0f') + format(income, '12,.0f'))
    year += 1
    income = income * 1.03
    save = income * percent
    savings = savings * 1.06
    savings += save
