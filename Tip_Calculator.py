print("Welcome to our Restaurant...")
# Get input from the user
num_people = int(input("How many People are in your Group? "))
# Ask user to choose a currency
currency = input("Choose a currency between $ or €: ")

# Check if the currency is valid
while currency != '$' and currency != '€':
    print("Warning: Invalid currency selected. Please choose either $ or €.")
    currency = input("Choose a currency between $ or €: ")

# If we reach this point, we know the currency is valid
print(f"You chose {currency}")
total_cost = float(input("What was the total Cost of the Lunch? "))
tip_percent = float(input("What percentage Tip would you like to leave? "))


# Calculate the tip and the cost per person
tip_amount = total_cost * tip_percent / 100
total_cost += tip_amount
cost_per_person = total_cost / num_people

# Print the results
print(f"The Total Cost of the Lunch is {total_cost:.2f}{currency}")
print(f"The Tip amount is {tip_amount:.2f}{currency}")
print(f"The Cost per Person is {cost_per_person:.2f}{currency}")
print("Thank you for visiting our restaurant! We hope you enjoyed your Lunch.")