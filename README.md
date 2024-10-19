Here is a sample `README.md` formatted for GitHub:

```markdown
# Peanut Allergy Adventure Game

## Description
The **Peanut Allergy Adventure Game** is a text-based adventure game where players collect safe foods while navigating through various rooms. The challenge is to avoid the pantry, which contains peanut butter. Players must gather all safe foods before accidentally entering the pantry to win.

The game adheres to industry-standard best practices, including clear naming conventions, in-line comments, and well-organized code. It is implemented in Python and follows PEP 8 guidelines.

## Gameplay
Players interact with the game by typing commands. You can move through rooms, collect items, and win by retrieving all the safe foods. However, entering the pantry, which contains a peanut-containing item, ends the game.

### Commands:
- **Move:** Type `North`, `South`, `East`, or `West` to move in that direction.
- **Pick an Item:** Type `'pick'` to collect an item in the current room.

### Objective:
- Collect all the **safe foods** (e.g., Apple, Baby Formula, Water) while avoiding peanuts.
- **Winning:** Successfully collect all the safe foods.
- **Losing:** Enter the Pantry room containing **Peanut Butter** before collecting all the safe foods.

## How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/AndriannaMitchell/TextBasedGAme.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TextBasedGame
   ```
3. Run the game:
   ```bash
   python TextBasedGame.py
   ```
4. Follow the on-screen instructions to move between rooms and collect items.

## Example Gameplay

```text
Welcome to the Peanut Allergy Adventure Game!
Your goal is to collect all safe foods while avoiding peanuts.
You can move between rooms using directions: North, South, East, West.
To collect an item, type 'pick'.
Good luck!

You are in the Living Room.
Inventory: []
You see: []
----------------------
Enter direction to move (North, South, East, West), or 'pick' to gather an item: North

You are in the Bedroom.
Inventory: []
You see: ['Baby Formula']
----------------------
Enter direction to move (North, South, East, West), or 'pick' to gather an item: pick
You have picked up Baby Formula.
```

## Requirements
- Python 3.x

## Features
- Navigate through rooms using directional commands.
- Collect safe foods and avoid the pantry.
- Input validation to handle invalid commands.

## Contributing
If you'd like to contribute to the development of the game, feel free to fork the repository and submit a pull request with your changes. 

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-branch`
6. Open a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

You can modify the repository URL under the "How to Play" section with your GitHub username or organization name.
