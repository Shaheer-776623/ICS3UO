Birth_year = input("Please type your year of birth:")
Birth_year = int(Birth_year)
Age = input("\nPlease type your current age: ")
Age = int(Age)

Calculation = Birth_year * 2 + 5
Calculation = int(Calculation)
Calculation = int(Calculation) * 50 + Age
Calculation = Calculation - 250
Calculation = Calculation / 100

print ("\nAfter a series of calculations the number we get is: ", Calculation)

print ("\nTo get this number we doubled your date of birth then added 5. We then multiplied the result by 50 and added your age. Lastly we subtracted the result by 250 then divided it by 100. In result we got your birth year as the number, and your age as the decimal.")
