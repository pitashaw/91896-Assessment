# Calculate the ticket price based on the age
def calc_pizza_price(var_age):

    # pizza is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # pizza is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # pizza price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price

#loop for testing...
while True:

    # Get age (assume users input a valid integer)
    age = int(input("Age: "))

    # calculate ticket cost
    pizza_cost = calc_pizza_price(age)
    print("Age: {}, Pizza Price: ${:.2f}".format(age, pizza_cost))