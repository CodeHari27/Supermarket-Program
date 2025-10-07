money = 1000
print(f"Having {money}$ in your bank account, you enter a supermarket to buy groceries.")
applePrice= 20
bananaPrice = 25
onionPrice = 15
tomatoPrice = 30
biscuitsPrice = 5
browniesPrice = 7
item = "nothing"
expenditure = 0
choice = 0
cost = 0
while choice != "enough":
    print("There are the following items to buy: \na. Apples - 20$\nb. Bananas - 25$\nc. Onions - 15$\nd. Tomatoes - 30$\ne. Biscuits - 5$\nf. Brownies - 7$")
    choice = input("Enter your choice and \"enough\" to buy the selected items in their respective amounts: ")
    if choice in ['a', 'b', 'c', 'd', 'e', 'f',"enough"]:
        if choice == 'a':
            cost = 0
            item = "apple"
            amount = int(input(f"Enter the amount of {item}s to be purchased: "))
            cost = applePrice * amount
            if expenditure + cost > money:
                print("You don't have enough money.")
            else:
                expenditure += cost
                print(f"Purchased {amount} {item}(s). Remaining: {money - expenditure}$")
        if choice == 'b':
            cost = 0
            item = "banana"
            amount = int(input(f"Enter the amount of {item}s to be purchased: "))
            cost = bananaPrice * amount
            if expenditure + cost > money:
                print("You don't have enough money.")
            else:
                expenditure += cost
                print(f"Purchased {amount} {item}(s). Remaining: {money - expenditure}$")
        if choice == 'c':
            cost = 0
            item = "onion"
            amount = int(input(f"Enter the amount of {item}s to be purchased: "))
            cost = onionPrice * amount
            if expenditure + cost > money:
                print("You don't have enough money.")
            else:
                expenditure += cost
                print(f"Purchased {amount} {item}(s). Remaining: {money - expenditure}$")
        if choice == 'd':
            cost = 0
            item = "tomato"
            amount = int(input(f"Enter the amount of {item}s to be purchased: "))
            cost = tomatoPrice * amount
            if expenditure + cost > money:
                print("You don't have enough money.")
            else:
                expenditure += cost
                print(f"Purchased {amount} {item}(s). Remaining: {money - expenditure}$")
        if choice == 'e':
            cost = 0
            item = "biscuit"
            amount = int(input(f"Enter the amount of {item}s to be purchased: "))
            cost = biscuitsPrice * amount
            if expenditure + cost > money:
                print("You don't have enough money.")
            else:
                expenditure += cost
                print(f"Purchased {amount} {item}(s). Remaining: {money - expenditure}$")
        if choice == 'f':
            cost = 0
            item = "brownie"
            amount = int(input(f"Enter the amount of {item}s to be purchased: "))
            cost = browniesPrice * amount
            if expenditure + cost > money:
                print("You don't have enough money.")
            else:
                expenditure += cost
                print(f"Purchased {amount} {item}(s). Remaining: {money - expenditure}$")
    elif choice not in ['a', 'b', 'c', 'd', 'e', 'f', "enough"]:
        print("Wrong choice! Try again.")
if choice == "enough":
    print("Bought all the items! Thank you.")
    


