# Secret Santa Texter
# Texts the people who wants to give a gift to to keep it anonymous
import random

# Initialize an empty list to store the names, addresses, and phone numbers
entries = []

# Ask the User for the entries of the people participating
print("Secret Sata Texter")
print("Hello, please put in every detail of the people participating individually.")
print("After giving the details, this program will text the people seperately.")

while True:
    name = input("Enter name (or type 'done' to finish): ")
    print()

    # Check if the user wants to stop
    if name.lower() == 'done':
        break

    address = input(f"Enter the address of {name}: ")
    print()

    phone_number = input(f"Enter the phone number of {name}: ")
    print()

    # Append the collected entry as a tuple to the list
    entries.append((name, address, phone_number))

# Randomize the participants to send the texts to
random.shuffle(entries)

# Display the enteries
for entry in entries:
    print(f"name: {entry[0]}, address: {entry[1]}, phone number: {entry[2]}")