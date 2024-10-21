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

# Set the giver list the same elements as the participants list
givers = participants[:]

# Randomize the participants that the givers will send a gift to
random.shuffle(participants)

# Go thru each participant and assign the gifters their person to send a gift too
# And text each gifter the information of the receiver
for i in range(len(givers)):
    # If a giver is paired with themselves reshuffle
    while (givers[i] == participants[0]):
        random.shuffle(participants)

    receivers.append(participants.pop(0))

    # Debug
    print(f"{givers[i][0]} is Secret Santa for {receivers[i][0]}")

    message = f"Merry Early Xmas {givers[i][0]}! This is a Secret Santa Texting program! Your person Secret Santa is {receivers[i][0]}. The address to ship their gift is {receivers[i][1]}."

    #TODO Send texts to the participants
    print(message)