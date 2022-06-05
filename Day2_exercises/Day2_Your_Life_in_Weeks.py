# simple program to calculate how many days/weeks/months we have left till we become 90 years
age = input("What is your current age? ")
age_difference = 90 - int(age)

days_till_90 = age_difference * 365
weeks_till_90 = age_difference * 52
months_till_90 = age_difference * 12

print(f"You have {days_till_90} days, {weeks_till_90} weeks, {months_till_90} months")