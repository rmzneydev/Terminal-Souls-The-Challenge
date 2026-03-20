import random

from turnoJugador import (playerTurn)
from turnoEnemigo import (enemyTurn)
from commons import (show_state, verify_winner)


hp_hero = 100
hp_enemy = 120
potions = 3  


heroName = "Shreck 🧌"
enemyName = "Nemesis ☠️"


winner = verify_winner(hp_hero, hp_enemy)



S
while winner == False:



    show_state(heroName, hp_hero, enemyName, hp_enemy, potions)


    # Player Turn

    hp_hero, hp_enemy, potions = playerTurn(hp_hero, hp_enemy, potions)
    

    hp_hero = enemyTurn(hp_hero)

    winner = verify_winner(hp_hero, hp_enemy)

    # Check if the enemy died
    if hp_enemy == 0:
        print("\n 💥¡YOU WIN!💥")
       

    # Check if the player died
    if hp_hero == 0:
        print("\n 💀¡YOU LOSE!💀")
      
        
