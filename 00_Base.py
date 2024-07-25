

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
            elif response== item[0]:
                return item


        print(error)

# shows menu
def show_menu():
    print('''\n
***** Menu *****
Pizza                   Regular Large
1.Cheese                $7.00  $10.00
2.Hawaiian              $7.00  $10.00
3.Margherita            $7.00  $10.00
4.Pepperoni             $7.00  $10.00
5.Meatlovers            $10.00 $13.00
6.Chicken Supreme       $10.00 $13.00
7.Crispy BBQ Pork Belly $10.00 $13.00
8.Lamb Kebab            $10.00 $13.00
9.Peri Peri Chicken     $15.00 $18.00
10.Chicken & Camembert  $15.00 $18.00

Regular: 12 Inches
Large: 14 Inches

Extra Toppings
1.Feta Cheese     $1.50
2.Pepperoni       $1.00
3.Mushrooms       $0.75
4.Green Peppers   $0.50
5.Black Olives    $0.75
6.Italian Sausage $1.25
7.Red Onions      $0.75
8.Spinach         $1.00
9.Bacon           $1.50
10.Tomatoes       $0.75

Order a MAXIMUM of 5 pizzas

******************************''')
# Main Routine goes here

print("Welcome to Pita's Pizzaria")

# set maximum number of pizzas
MAX_PIZZAS = 5

yes_no_list = ["yes", "no"]
delivery_option = ["delivery", "pickup"]

# List to hold pizza details
all_name = ["1.Cheese", "2.Hawaiian", "3.Margherita", "4.Pepperoni", "5.Meatlovers",
            "6.Chicken Supreme", "7.Crispy BBQ Pork Belly", "8.Lamb Kebab", "9.Peri Peri Chicken",
            "10.Chicken and Camembert"]
regular_pizza_cost =["1.$7.00", "2.$7.00", "3.$7.00", "4.$7.00", "5.$10.00",
                    "6.$10.00", "7.$10.00", "8.$10.00", "9.$15.00", "10.$15.00"]
large_pizza_cost = ["1.$10.00", "2.$10.00", "3.$10.00", "4.$10.00", "5.$13.00",
                    "6.$13.00", "7.$13.00", "8.$13.00", "9.$18.00", "10.$18.00"]
all_surcharge = []
all_size_pizza = []

# Dictionary used  to create data frame ie: column_name:
pizza_order_dict = {
    "Name": all_name,
    "Regular Pizza Cost": regular_pizza_cost,
    "Large Pizza Cost": large_pizza_cost,
    "Surcharge": all_surcharge,
    "Size of Pizza": all_size_pizza
}

# Select name for order
name = not_blank("Please enter your name for order ")

# Ask if user wants pickup or delivery

delivery = string_checker("Do you want pickup or delivery?", delivery_option)

if delivery == "delivery":
    print("There is a $6 surcharge")

# Would you like to place an order
while True:
    want_order = yes_no("Would you like to place"
                        " an order?")

    if want_order == "yes":
        print(show_menu())

        print()

    else:
        break

print("Thank you")

# add item, quantity and price to lists-
item_list.append(item_name)
quantity_list.append(quantity)
price_list.append(price)

expense_frame = pandas.DataFrame(variable_dict)
expense_frame = expense_frame.set_index('Item')

# Calculate cost of each component
expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame

# Find sub-total
sub_total = expense_frame['Cost'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    expense_frame[item] = expense_frame[item].apply(currency)

return [expense_frame, sub_total]

# loop to sell pizzas









