print("Welcome to the tip calculator!")

bill = float(input("what is the total bill?"))

people = float(input("How many people do you want to spilt the bill with?"))

percent = float(input("What percentage tip would like to give? 10, 12 or 15"))

bill_per_person = (bill / people) + ((bill / people) * (percent / 100))

print("Each of you will pay $", "{:.2f}".format(bill_per_person))

