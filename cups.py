# This code prints the price for a user defined number cups of coffee.

price = input("What is the price of coffee?")
cups = input("How many cups are do you want?")
total = float(price) * int(cups)
print("Your total is $" + str(total) + " for " + cups + " cups.")
