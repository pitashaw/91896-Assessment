
import pandas as pd

# Functions go here

# Stops users entering a blank input
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response

# Stops users from entering a non valid name
def name_check(question):
    while True:
        response = input(question).strip()
        if response == "" or not response.isalpha():
            print("Sorry, please enter a name using only letters.")
        else:
            return response

# Checks users input valid numbers
def num_check(question, min_value=None, max_value=None):
    while True:
        try:
            response = int(input(question))
            if (min_value is not None and response < min_value) or (max_value is not None and response > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return response
        except ValueError:
            print("Please enter an integer.")

# Allows users to enter shorter inputs instead of writing out full input.
def string_checker(question,num, valid_responses):
    while True:
        error = f"Please enter a valid response from {valid_responses}"
        response = input(question).lower()

        for item in valid_responses:
            if item == response or response == item[:num]:
                return item
        print(error)

# Formatting for price display
def currency(x):
    return "${:.2f}".format(x)

# Checks number input and assigns pizza to the value
def pizza_id_checker(id):
    pizza_dict = {
        1: "Cheese", 2: "Hawaiian", 3: "Margherita", 4: "Pepperoni", 5: "Meatlovers",
        6: "Chicken Supreme", 7: "Crispy BBQ Pork Belly", 8: "Lamb Kebab",
        9: "Peri Peri Chicken", 10: "Chicken & Camembert"
    }
    return pizza_dict.get(id, "Unknown Pizza")

# Checks number input and assigns pizza to the value
def topping_id_checker(id):
    if id < 1 or id > 10:
        return ("Invalid Topping ID", 0)
    topping_dict = {
        1: ("Feta Cheese", 1.50), 2: ("Pepperoni", 1.00), 3: ("Mushrooms", 0.75),
        4: ("Green Peppers", 0.50), 5: ("Black Olives", 0.75), 6: ("Italian Sausage", 1.25),
        7: ("Red Onions", 0.75), 8: ("Spinach", 1.00), 9: ("Bacon", 1.50),
        10: ("Tomatoes", 0.75)
    }
    return topping_dict.get(id, ("Unknown Topping", 0))

#
def phone_number_check(question):
    while True:
        response = input(question).strip()
        if response.isdigit() and len(response) >= 10:
            return response
        else:
            print("Please enter a valid phone number with at least 10 digits.")


# Main Routine
print("Welcome to Pita's Pizzaria")

MAX_PIZZAS = 5
MAX_TOPPINGS = 3
yes_no_list = ["yes", "no"]
delivery_option = ["delivery", "pickup"]
size_option = ["regular", "large"]
payment_option = ["cash", "credit"]

pizza_menu_dict = {
    "Name": ["Cheese", "Hawaiian", "Margherita", "Pepperoni", "Meatlovers",
             "Chicken Supreme", "Crispy BBQ Pork Belly", "Lamb Kebab", "Peri Peri Chicken",
             "Chicken and Camembert"],
    "Regular Pizza Cost": ["$7.00"]*10,
    "Large Pizza Cost": ["$10.00"]*10
}

toppings_menu_dict = {
    "Toppings": ["Feta Cheese", "Pepperoni", "Mushrooms", "Green Peppers",
                 "Black Olives", "Italian Sausage", "Red Onions", "Spinach",
                 "Bacon", "Tomatoes"],
    "Price": ["$1.50", "$1.00", "$0.75", "$0.50", "$0.75", "$1.25",
              "$0.75", "$1.00", "$1.50", "$0.75"]
}

menu_frame = pd.DataFrame(pizza_menu_dict)
menu_frame.index += 1
toppings_menu_frame = pd.DataFrame(toppings_menu_dict)
toppings_menu_frame.index += 1

name = name_check("Please enter your name for the order: ")

delivery = string_checker("Do you want pickup or delivery? ",1, delivery_option)

if delivery == "delivery":
    print("There is a $6 surcharge.")
    total_cost = 6.0
    phone_number = phone_number_check("Please enter your phone number: ")
    address = not_blank("Please enter your delivery address: ")
else:
    total_cost = 0

while True:  # Loop for placing orders
    user_order = []
    all_size_pizza = []
    all_pizza_cost = []
    all_topping = []
    all_topping_price = []
    all_order_totals = []

    while len(user_order) < MAX_PIZZAS:
        print(menu_frame)
        print()

        user_order_id = num_check("Please enter the number of the pizza you want to order (1-10): ", min_value=1, max_value=10)
        user_order_name = pizza_id_checker(user_order_id)
        size_pizza = string_checker("What size would you like? (regular/large): ", 1,size_option)

        cost = 7 if size_pizza == "regular" else 10

        topping_list = []
        topping_price_list = []
        topping_total_cost = 0

        want_toppings = string_checker("Would you like to add extra toppings? ", 1,yes_no_list)
        while want_toppings == "yes" and len(topping_list) < MAX_TOPPINGS:
            print(toppings_menu_frame)
            topping_order_id = num_check("Please enter the number of the topping you want to order (1-10): ", min_value=1, max_value=10)
            topping_order_name, topping_cost = topping_id_checker(topping_order_id)

            if topping_order_name == "Invalid Topping ID":
                print("Invalid topping ID. Please enter a number between 1 and 10.")
                continue

            topping_list.append(topping_order_name)
            topping_price_list.append(currency(topping_cost))
            topping_total_cost += topping_cost

            if len(topping_list) < MAX_TOPPINGS:
                want_toppings = string_checker("Would you like to add another topping? ",1, yes_no_list)
            else:
                print(f"You've reached the maximum of {MAX_TOPPINGS} toppings.")

        # Add the pizza cost and total topping cost to the total
        total_cost += cost + topping_total_cost

        user_order.append(user_order_name)
        all_size_pizza.append(size_pizza)
        all_pizza_cost.append(currency(cost))
        all_topping.append(", ".join(topping_list) if topping_list else "None")
        all_topping_price.append(", ".join(topping_price_list) if topping_price_list else "$0.00")
        all_order_totals.append(currency(cost + topping_total_cost))

        if len(user_order) >= MAX_PIZZAS:
            print(f"You've reached the maximum of {MAX_PIZZAS} pizzas.")
            break
        else:
            more_pizza = string_checker("Would you like to order another pizza? (yes/no): ", 1,yes_no_list)
            if more_pizza == "no":
                break

    pizza_order_dict = {
        "Pizza": user_order,
        "Size": all_size_pizza,
        "Toppings": all_topping,
        "Topping Prices": all_topping_price,
        "Pizza Price": all_pizza_cost,
        "Total Price": all_order_totals
    }

    order_frame = pd.DataFrame(pizza_order_dict)

    # Printing the order summary vertically
    print("\nYour Order Summary:")
    for index, row in order_frame.iterrows():
        print(f"Pizza {index+1}:")
        print(f"  - Name: {row['Pizza']}")
        print(f"  - Size: {row['Size']}")
        print(f"  - Toppings: {row['Toppings']}")
        print(f"  - Topping Prices: {row['Topping Prices']}")
        print(f"  - Pizza Price: {row['Pizza Price']}")
        print(f"  - Total Price: {row['Total Price']}\n")

    # Select payment method
    payment_method = string_checker("How would you like to pay (cash/credit)? ", 2,payment_option)

    if payment_method == "credit":
        print("There is a 2% surcharge for credit payments.")
        surcharge = total_cost * 0.02
        total_cost += surcharge
        print(f"Surcharge: {currency(surcharge)}")

    print(f"The total price would be {currency(total_cost)}")
    if delivery == "delivery":
        print(f"Your pizza will be delivered to {address}. We will contact you at {phone_number} if needed.")

    confirm_order = string_checker("Do you want to confirm the order (yes/no)? ",1, yes_no_list)

    if confirm_order == "yes":
        print(f"Thank you! Your order has been confirmed. You will pay with {payment_method}.")
    else:
        print("Your order has been canceled.")

    # Ask if the user would like to place another order
    another_order = string_checker("Would you like to place another order? (yes/no): ", 1,yes_no_list)
    if another_order == "no":
        print("Thank you for visiting Pita's Pizzaria! Goodbye!")
        break
