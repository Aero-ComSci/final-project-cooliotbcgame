TBC Concept Showcase
(README done by AI)
This project is a simple turn-based combat simulator implemented in Python.

Who is this program for?
This program is primarily for individuals who enjoy simple, interactive text-based games. It can also be a useful example for those learning basic Python programming concepts, particularly:

Object-oriented programming (OOP) through the combatant class.
Working with lists and other data structures.
Implementing game loops and turn-based logic.
Basic input and output operations in Python.
What does this program do? What does it automate?
This program simulates a battle between a player-controlled combatant and a computer-controlled enemy. It automates the following aspects of a simple combat scenario:

Character Definition: It allows you to define combatants with different attributes like name, attack strengths, defense (heal), and health points.
Turn-Based Gameplay: It manages the flow of combat, allowing the player to choose an action (attack or heal) in their turn, followed by a random action from the enemy.
Action Resolution: It calculates and applies damage or healing based on the chosen actions.
Game End Condition: It determines the winner (or a draw) based on the health points of the combatants reaching zero.
Random Enemy Actions: The enemy's actions (which attack to use or whether to heal) are chosen randomly, providing a degree of unpredictability.
Video/Screenshots
Video Demonstration: [Link to your video here]

&lt;p align="center">
&lt;img src="path/to/your/screenshot1.png" alt="Screenshot of the game" width="400">
&lt;br>
Screenshot of a combat turn.
&lt;/p>
&lt;p align="center">
&lt;img src="path/to/your/screenshot2.png" alt="Another screenshot" width="400">
&lt;br>
Screenshot showing the combatant stats.
&lt;/p>

Keep your video and screenshot files in a location that GitHub can access (usually within your repository). Update the src attributes in the <img> tags and the video link accordingly.

Installation
No explicit installation is required as this is a Python script. Ensure you have Python 3.x installed on your system.

How to Run the Program
Save the combatant.py, epic.py, and main.py files in the same directory.
Open a terminal or command prompt and navigate to that directory.
Run the main script using the command: python main.py
Code Samples
Here are a few code samples from the project demonstrating specific Python concepts:

1. Using a collection (list) in the combatant class:

This get_options method in the combatant class demonstrates the use of a list to store the combatant's available actions:

```python
def get_options(self):
Atks = []
Atks.append(self.atk)
Atks.append(self.atk2)
Atks.append(self.atk3)
Atks.append(self.def1)
return Atks
```

2. Using a loop in the main game logic:

The while ongoing: loop in epic.py controls the main game flow, continuing until a win/lose/draw condition is met:

```python
ongoing = True
while ongoing:
print("Here are the combatants and their stats!")
combatants = [player, enemy]
for i in combatants:
print(i)
# ... rest of the game logic ...
```

3. Using a function (method) in the combatant class:

The __str__ method is a special function in Python that defines how an object of the combatant class should be represented as a string:

```python
def str(self):
bob = ""
bob += str("Combatant: " + self.name + ": ")
bob += str("Attack 1: " + str(self.atk) + ", ")
bob += str("Attack 2: " + str(self.atk2) + ", ")
bob += str("Attack 3: " + str(self.atk3) + ", ")
bob += str("Heal: " + str(self.def1) + ", ")
bob += str("Health: " + str(self.hp) + ", ")
return bob
```
