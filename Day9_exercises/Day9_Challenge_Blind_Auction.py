import os
# a small blind bidding program
print(r'''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ ''')
print("Welcome to the secret auction program")
bidder = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidder[name] = bid
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if add_bidder == "yes":
        os.system('cls')
    elif add_bidder == "no":
        break

def find_highest_bidder(record):
    highest_bid = 0
    winner = ""

    for key in record:
        if record[key] > highest_bid:
            highest_bid = record[key]
            winner = key

    print(f"Highest bid is ${highest_bid}, {winner} wins the auction!")
    input()

find_highest_bidder(bidder)
