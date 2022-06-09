# calculating the sum of even numbers from 1-100

summation = 0
for number in range(1, 101):
    if number % 2 == 0:
        summation += number
print(f"The output is: {summation}")