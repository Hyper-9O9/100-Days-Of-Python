two_digit_number = input("Type a two digit number:")

while(True):
    if(len(two_digit_number) == 2):
        a = int(two_digit_number[0])
        b = int(two_digit_number[1])
        print(a+b)
        break
    else:
        print("Please enter a two digit number")
        two_digit_number = input("Type a two digit number:")