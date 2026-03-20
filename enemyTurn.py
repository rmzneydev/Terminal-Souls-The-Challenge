
from commons import(generate_damage, critical_system)




def enemyTurn(hp_hero):

    print("\n ------☠️ ENEMY TURN ☠️------\n")

    damage = generate_damage(15, 20)
    damage = critical_system(damage)
    hp_hero -= damage

    if hp_hero < 0:
        hp_hero = 0

    print(f'The enemy attacked you and did {damage} damage')
    print(f'Your life now is: {hp_hero}\n') #New Life Player


    return hp_hero

