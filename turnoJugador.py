import random

from commons import (generate_damage,critical_system)



# hp_hero = 60
# hp_enemy = 120
# potions = 3  


def playerTurn(hp_hero, hp_enemy, potions):


    turno_valido = False

    while turno_valido == False:

        print("\n ------🧌  YOUR TURN 🧌------\n")
        print("1. Attack")
        print("2. Cure")
        print("3. Special Hability")

        try:
            selection = int(input("\n Select the action: "))
        except ValueError:
            print("Error, enter valid value")
            continue
        
        # Attack (Aleatory damage between 10-25)

        if selection == 1:
            damage = generate_damage(10,25)
            damage = critical_system(damage)
            hp_enemy -= damage

            if hp_enemy < 0:
                hp_enemy = 0
            print(f'You dealt {damage} damage. Monster have {hp_enemy} of health remaining.')
            

            turno_valido = True
            
        # Cure (recupera 20 HP solo si tiene posiones)

        elif selection == 2:

            if potions > 0: 
                healthBefore = hp_hero #Guardar la vida antes de operar

                hp_hero = hp_hero + 20 # Sumar la posion

                if hp_hero > 100: #Limitar la vida máxima
                    hp_hero = 100
                
                healing = hp_hero - healthBefore
                potions -= 1

                if healing > 0:
                    print(f'You were cured... {healing} HP')
                else:
                    print("You have the maximum life")
                

                print(f'Your life is:: {hp_hero}')
                print(f'You have {potions} potions')
            else: 
                print("You haven't potions")
                continue

            turno_valido = True

        # Special Hability (High damage between 30-50 but with a 50% chance of hitting)

        elif selection == 3:

            prob = random.random()

            if prob <= 0.5:

                damage = generate_damage(30,50) # Dame function here
                damage = critical_system(damage)
                hp_enemy -= damage

                print(f'Successful special ability! You did {damage} damage')

            else:
                print("Special ability failure")

            turno_valido = True

        else: 
            print("Invalid option")

    return hp_hero, hp_enemy, potions



# hp_hero, hp_enemy, potions = turno_jugador(hp_hero, hp_enemy, potions)