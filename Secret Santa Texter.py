# Secret Santa Texter
import random

# Initialize an empty list to store the names, addresses, and phone numbers
entries = []

while True:
    name = input("Enter name (or type 'done' to finish): ")

    # Check if the user wants to stop
    if name.lower() == 'done':
        break

    address = input(f"Enter the address of {name}: ")

    phone_number = input(f"Enter the phone number of {name}: ")

    # Append the collected entry as a tuple to the list
    entries.append((name, address, phone_number))

# Display the enteries
for entry in entries:
    print(f"name: {entry[0]}, address: {entry[1]}, phone number: {entry[2]}")