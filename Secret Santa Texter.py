# Secret Santa Texter
# Texts the people who wants to give a gift to to keep it anonymous
import random
import os
from dotenv import load_dotenv

#TODO find an free api to send texts

# Load enviroment variables from .env file
load_dotenv()

# Retrieve sensitive information from enviornment variables


# Initialize empty lists to store the names, addresses, and phone numbers
participants = [] # People that are participating
receivers = [] # People that receives the gift
givers = [] # People that gives the gitft

# Display the header of the program
print("Secret Sata Texter")
print("Hello, please put in every detail of the people participating individually.")
print("After giving the details, this program will text the people seperately.")

# Ask the User for the budget
budget = input("Enter the amount for the Budget: ")
print()

# Ask the User for the entries of the people participating
while True:
    # Check that we have enough participants
    if len(participants) < 2:
        print("Need at least 2 participants for Secret Santa!")

    name = input("Enter name (or type 'done' to finish): ")
    print()

    # Check if the user wants to stop
    if name.lower() == 'done':
        break

    address = input(f"Enter the address of {name} (or type 'N/A' for no address): ")
    print()

    phone_number = input(f"Enter the phone number of {name}: ")
    print()

    # Append the collected entry as a tuple to the list
    participants.append((name, address, phone_number))

file_flag = True if input("Would you like a .txt file instead of texting? (Type Y for yes and N for no)").lower() == 'y' else False
print()
if file_flag:
    print("The output file is output.txt")
    with open("output.txt", "w") as file:
        file.write("")

# Set the lists the same elements as the participants list
givers = participants[:]
receivers = participants[:]

# Shuffle the receivers list to randomize the pairings
random.shuffle(receivers)

# Re-shuffle if someone is paired with themselves
while any(giver == receiver for giver, receiver in zip(givers, receivers)):
    random.shuffle(receivers)

# Text each gifter the information of the receiver
for giver, receiver in zip(givers, receivers):
    # Message for sending the gifter about who is their Secret Santa
    message = f"Merry Xmas {giver[0]}! Your Secret Santa is {receiver[0]} and the budget is ${budget}. The address to ship their gift is {receiver[1]}."

    if file_flag:
        with open("output.txt", "a") as file:
            file.write(message + "\n")
    else:
        #TODO Send texts to the participants
        print(message)