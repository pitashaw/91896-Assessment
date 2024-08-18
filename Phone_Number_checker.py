def phone_number_check(question):
    while True:
        response = input(question).strip()
        if response.isdigit() and len(response) >= 10:
            return response
        else:
            print("Please enter a valid phone number with at least 10 digits.")


#Main Routine

phone_number = phone_number_check("Please enter your phone number: ")