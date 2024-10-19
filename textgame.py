# TextBasedGame.py
# This script is a text-based adventure game where the player collects safe foods while avoiding peanuts.
# Author: [Andrianna Mitchell]


# Game dictionary to store room navigation and items
rooms = {
    'Living Room': {
        'South': 'Dining Room',
        'North': 'Bedroom',
        'East': 'Playroom',
        'West': 'Kitchen',
        'items': []
    },
    'Bedroom': {
        'South': 'Living Room',
        'East': 'Garden',
        'items': ['Baby Formula']
    },
    'Garden': {
        'West': 'Bedroom',
        'items': ['Berries']
    },
    'Dining Room': {
        'North': 'Living Room',
        'East': 'Basement',
        'items': ['Apple']
    },
    'Basement': {
        'West': 'Dining Room',
        'items': ['Water']
    },
    'Playroom': {
        'West': 'Living Room',
        'North': 'Pantry',
        'items': ['Rice Crackers']
    },
    'Kitchen': {
        'East': 'Living Room',
        'items': ['Veggies']
    },
    'Pantry': {
        'South': 'Playroom',
        'items': ['Peanut Butter']  # Peanut-containing food
    }
}


# List of all safe foods
safe_foods = [
    'Baby Formula', 'Berries', 'Apple',
    'Water', 'Rice Crackers', 'Veggies'
]


# Function to display game instructions
def show_instructions():
    """Display the instructions for the game."""
    print("Welcome to the Peanut Allergy Adventure Game!")
    print("Your goal is to collect all safe foods while avoiding peanuts.")
    print("You can move between rooms using directions: North, South, East, West.")
    print("To collect an item, type 'pick'.")
    print("Good luck!\n")


# Function to display the player's status
def display_status(current_room, inventory):
    """Display the player's current status."""
    print(f"\nYou are in the {current_room}.")
    print(f"Inventory: {inventory}")
    print(f"You see: {rooms[current_room]['items']}")
    print("----------------------")


# Main game function
def main():
    """Main function to run the game logic."""
    # Initialization
    inventory = []  # Start with an empty inventory
    current_room = 'Living Room'  # Start in the Living Room

    show_instructions()  # Show the game instructions

    # Main game loop
    while set(safe_foods).difference(inventory):  # Continue until all safe foods are collected
        display_status(current_room, inventory)  # Display current status

        # Prompt for user input
        user_input = input(
            "Enter direction to move (North, South, East, West) or 'pick' to gather an item: "
        ).strip()

        if user_input == "pick":  # Picking an item
            if rooms[current_room]['items']:  # Check if there are items to pick
                for item in rooms[current_room]['items']:
                    if item != "Peanut Butter":
                        inventory.append(item)
                        print(f"You have picked up {item}.")
                        rooms[current_room]['items'].remove(item)
                if "Peanut Butter" in rooms[current_room]['items']:
                    print("You entered the pantry! The baby has an allergic reaction. Game Over.")
                    break  # End the game
            else:
                print("No items to pick up in this room!")

        else:  # Moving between rooms
            direction = user_input.capitalize()
            if direction in rooms[current_room]:  # Check if direction is valid
                current_room = rooms[current_room][direction]
                if current_room == "Pantry":  # Check if moved to pantry
                    print("You entered the pantry! The baby has an allergic reaction. Game Over.")
                    break  # End the game
            else:
                print("Invalid input! You can't move that way. Please enter North, South, East, or West.")

    if set(safe_foods).issubset(inventory):  # Check if all safe foods are collected
        print("Congratulations! You collected all safe foods.")


# Run the game
if __name__ == "__main__":
    main()
