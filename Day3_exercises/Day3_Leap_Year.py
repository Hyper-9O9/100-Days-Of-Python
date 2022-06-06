# checking if a year is a leap year or not
# Rules:
# if the number evenly divisible by 4, it means it is likely to be a leap year
# if the number is not evenly divisible by 100 it is a leap year
    # if it is divisibile evenly by 100
        # divide it by 400 if it is even then it is leap year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")



