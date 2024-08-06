import pandas


# functions go here
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# checks users enter an integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# Calculate the pizza price based on the size
def calc_pizza_price(var_type):
    # pizza is $5.00 for 1,2,3,4
    if var_type < 5:
        price = 5.00

    # pizza is $10.50 for users between 16 and 64
    elif var_type < 65:
        price = 10.5

    # pizza price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# checks that users enter a valid response (e.g. yes/ no
# cash / credit) based on a list of options
def string_checker(question, valid_responses):
    while True:

        error = f"Please enter a valid response from {valid_responses}"

        response = input(question).lower()

        for item in valid_responses:
            if item == response:
                return item

            elif response == item[0]:
                return item

                print(error)

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Check what pizza is selected and assign the name
def pizza_id_checker(id):
    if id == 1:
        pizza = "Cheese"
    elif id == 2:
        pizza = "Hawaiian"
    elif id == 3:
        pizza = "Margherita"
    elif id == 4:
        pizza = "Pepperoni"
    elif id == 5:
        pizza = "Meatlovers"
    elif id == 6:
        pizza = "Chicken Supreme"
    elif id == 7:
        pizza = "Crispy BBQ Pork Belly"
    elif id == 8:
        pizza = "Lamb Kebab"
    elif id == 9:
        pizza = "Peri Peri Chicken"
    else:
        pizza = "Chicken & Camembert"

    return pizza
# Main Routine goes here

print("Welcome to Pita's Pizzaria")

# set maximum number of pizzas
MAX_PIZZAS = 5
want_order = ""

yes_no_list = ["yes", "no"]
delivery_option = ["delivery", "pickup"]
size_option = ["regular", "large"]

# List to hold pizza details
all_name = ["Cheese", "Hawaiian", "Margherita", "Pepperoni", "Meatlovers",
            "Chicken Supreme", "Crispy BBQ Pork Belly", "Lamb Kebab", "Peri Peri Chicken",
            "Chicken and Camembert"]
regular_pizza_cost =["$7.00", "$7.00", "$7.00", "$7.00", "$7.00",
                    "$7.00", "$7.00", "$7.00", "$7.00", "$7.00"]
large_pizza_cost = ["$10.00", "$10.00", "$10.00", "$10.00", "$10.00",
                    "$10.00", "$10.00", "$10.00", "$10.00", "$10.00"]
user_order = []
all_size_pizza = []
all_pizza_cost = []


# Check what pizza is selected and assign the name
all_order_totals = []
total_cost = 0

# Dictionary used  to create data frame ie: column_name:
pizza_order_dict = {
    "pizzas:": user_order,
    "size:": all_size_pizza,
    "price:": all_pizza_cost,
    "Total:": all_order_totals
}
pizza_menu_dict = {
    "Name": all_name,
    "Regular Pizza Cost": regular_pizza_cost,
    "Large Pizza Cost": large_pizza_cost
}

menu_frame = pandas.DataFrame(pizza_menu_dict)

# Select name for order
name = not_blank("Please enter your name for order ")

# Ask if user wants pickup or delivery

delivery = string_checker("Do you want pickup or delivery?", delivery_option)

if delivery == "delivery":
    print("There is a $6 surcharge")
    total_cost += 6.0

# Would you like to place an order
while want_order == "":

    print(menu_frame)

    print()

    user_order_id = num_check("Please enter the number of the pizza you want to order(1-10)")

    size_pizza = string_checker("What size would you like?(regular/large)", size_option)

    if size_pizza == "regular":
        cost = 7

    else:
        cost = 10

    user_order_name = pizza_id_checker(user_order_id)

    # Update the pizza_order_dict with order information

    # user_order.append(user_order_name)
    # all_size_pizza.append(size_pizza)
    # all_pizza_cost.append(cost)

    # Add the pizza cost to the total
    total_cost += cost

    # Update the order_dict with order information
    pizza_order_dict["pizzas:"].append(user_order_name)  # Add pizza name
    pizza_order_dict["size:"].append(size_pizza)  # Add size
    pizza_order_dict["price:"].append(cost)  # Add pizza price
    pizza_order_dict["Total:"].append(cost)  # Add total cost

    print(f"You have selected {user_order_name} {size_pizza} ${cost}")

    want_order = input("To order another pizza press enter or no to carry on ")

# add item, quantity and price to lists-
# all_name.append(all_name)
# regular_pizza_cost.append(regular_pizza_cost)
# large_pizza_cost.append(large_pizza_cost)


# Create the Order frame
order_frame = pandas.DataFrame(pizza_order_dict)
order_frame["price:"] = order_frame["price:"].apply(currency)
order_frame["Total:"] = order_frame["Total:"].apply(currency)

# expense_frame = pandas.DataFrame(pizza_order_dict)
# expense_frame = expense_frame.set_index('pizzas')

# Calculate cost of each component
# expense_frame['Cost'] = expense_frame['size'] * expense_frame

# Find sub-total
# sub_total = expense_frame['Cost'].sum()

# Currency Formatting (uses currency function)
# add_dollars = ['Price', 'Cost']
# for item in add_dollars:
#   expense_frame[item] = expense_frame[item].apply(currency)

print(order_frame.to_string(index=False, justify="left", col_space=15))
print("The total price would be ${:.2f}".format(total_cost))

print("Thank you")
