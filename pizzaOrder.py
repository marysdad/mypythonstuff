print("Welcome to Python Pizza Deliveries")

size = input("What size pizza do you want: s, m l") #$15, $20, $25
add_pepperoni = input("Do you wanto you want extra peppernori? y or n") # s2 or m/L3
extra_cheese = input("Do you want extra cheese? y or n" ) # $1
bill = 0

if size == "s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25

if size == "s" and add_pepperoni == "y":
    bill += 2
elif size == "m" or "l" and add_pepperoni == "y":
    bill += 3

if extra_cheese == "y":
    bill += 1

print("That will cost you a total of $" + str(bill))