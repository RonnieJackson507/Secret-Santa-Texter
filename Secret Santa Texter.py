# Secret Santa Texter
# Texts the people who wants to give a gift to to keep it anonymous
import random

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

    address = input(f"Enter the address of {name}: ")
    print()

    phone_number = input(f"Enter the phone number of {name}: ")
    print()

    # Append the collected entry as a tuple to the list
    participants.append((name, address, phone_number))

givers = participants[:]
receivers = []

# Randomize the participants that the givers will send a gift to
random.shuffle(participants)

for i in range(len(givers)):
    # If a giver is paired with themselves or if a receiver is already assigned, reshuffle
    while (givers[i] == participants[0]):
        random.shuffle(participants)

    receivers.append(participants.pop(0))

    # Debug
    print(f"{givers[i][0]} is Secret Santa for {receivers[i][0]}")

    #TODO Send texts to the participants

# Debug: Display the enteries
#for i in range(len(participants)):
#    print(f"name: {givers[i][0]}, address: {givers[i][1]}, phone number: {givers[i][2]}")
#    print(f"name: {receivers[i][0]}, address: {receivers[i][1]}, phone number: {receivers[i][2]}")