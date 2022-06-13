# a program to check if a nuber is prime or not
# prime numbers are those that are only divided by themselves and 1
# the code below is my initial approach
def prime_checker_1(number):
    dividers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    factors = 0
    if number > 9:
        dividers.append(number)
    for n in dividers:
        if number % number == 0 and number % n == 0:
            factors += 1
    if factors == 2:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


n = int(input("Check this number: "))
prime_checker_1(n)


# approach 2
def prime_checker_2(number):
    prime_flag = True

    for i in range (2,number):
        if number % i == 0:
            prime_flag = False
    if prime_flag is True:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
prime_checker_2(n)
