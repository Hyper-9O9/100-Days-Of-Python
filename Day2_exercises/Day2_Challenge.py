while(1==1):
    print("Welcome to the tip calculator.")

    total = float(input("What was the total of the bill? $"))
    people_number = float(input("How many people to split the bill? "))
    tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

    while(1==1):
        if(tip_percentage == 10):
            tip_percentage = 1.10
            break
        if(tip_percentage == 12):
            tip_percentage = 1.12
            break
        if(tip_percentage == 15):
            tip_percentage = 1.15
            break
        else:tip_percentage = float(input("Invalid number choose 10, 12, or 15: "))

    final_value = str(total/people_number*tip_percentage)
    print("Each person should pay : $" + final_value)
    print("Do you want to redo it? Y/N: ")
    answer = input()
    if(answer == "y"):
        continue
    if(answer == 'n'):
        print("Thanks for using the calculator")
        break



