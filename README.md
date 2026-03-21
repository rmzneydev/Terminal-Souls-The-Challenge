[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/rmzneydev/Terminal-Souls-The-Challenge)](https://github.com/rmzneydev/Terminal-Souls-The-Challenge/graphs/contributors)

# 🧌 Terminal Souls: The Challenge

A simple turn-based combat game built in Python where a hero battles an
enemy using attacks, healing, and special abilities. This project
demonstrates core programming concepts such as modular design, control
flow, and user interaction in a command-line interface.

------------------------------------------------------------------------

## 📌 Features

-   Turn-based combat system
-   Randomized damage mechanics
-   Critical hit system (10% chance to double damage)
-   Healing system using potions
-   Special ability with risk/reward mechanics
-   Visual game status display (HP bars)
-   Win/Lose condition detection

------------------------------------------------------------------------

## 🗂️ Project Structure

    .
    ├── main.py          # Game entry point
    ├── turnPlayer.py    # Player turn logic
    ├── enemyTurn.py     # Enemy turn logic
    ├── commons.py       # Shared utilities and helpers

------------------------------------------------------------------------

## 🚀 How to Run

### 1. Clone the repository

``` bash
git clone https://github.com/rmzneydev/Terminal-Souls-The-Challenge.git
cd Terminal-Souls-The-Challenge
```

### 2. Run the game

```bash
python main.py
```
------------------------------------------------------------------------

## 🎮 Gameplay

Each turn, the player can choose one of the following actions:

### 1. Attack

-   Deals random damage (10--25)
-   Can trigger a critical hit (x2 damage)

### 2. Cure

-   Restores 20 HP
-   Limited by available potions
-   Max HP is capped at 100

### 3. Special Ability

-   Deals high damage (30--50)
-   Only has a 50% chance to succeed

------------------------------------------------------------------------

## 🤖 Enemy Behavior

-   Automatically attacks each turn
-   Deals random damage (15--20)
-   Can also land critical hits

------------------------------------------------------------------------

## 📊 Game Mechanics

| Event Name | Description |
|------------|--------|
| HP System | Hero: 100 HP, Enemy: 120 HP |
| Critical Hits | 10% chance to double damage |
| Potions | Start with 3, each heals 20 HP |
| Win Condition | Enemy HP reaches 0 |
| Lose Condition | Hero HP reaches 0 |

------------------------------------------------------------------------

## 🧩 Key Functions

-   playerTurn(): Handles player decision-making and actions.
-   enemyTurn(): Executes enemy attack logic.
-   generate_damage(): Returns random damage within a given range.
-   critical_system(): Applies a chance-based damage multiplier.
-   show_state(): Displays the current game status with visual HP bars.
-   verify_winner(): Checks if the game has ended.

------------------------------------------------------------------------

## 💡 Concepts Demonstrated

-   Modular programming (multiple files)
-   Input validation and error handling
-   Random number generation
-   Game loop design
-   State management
-   CLI-based UI design

------------------------------------------------------------------------

## 📈 Possible Improvements

-   Add multiple enemies or levels
-   Implement experience and leveling system
-   Improve balance and difficulty scaling

------------------------------------------------------------------------

## 🔄 Flow Diagram

The following diagram represents the game loop and decision flow:

[Flow Diagram](https://drive.google.com/file/d/1grE8pYwJZe7KqGsDjQGshtRB0H7NBDyo/view)

------------------------------------------------------------------------
## Authors

Developed by **Andres Elles* and *Neyder Ramirez**
