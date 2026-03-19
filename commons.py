import random
def generate_damage(min, max):
    damage = random.randint(min, max)
    return damage

def show_state(hero_name, hero_hp, enemy_name, enemy_hp):
    max_hero_hp = 100
    max_enemy_hp = 120
    
    lost_hp = max_hero_hp - hero_hp
    print("#"*10, " GAME STATUS ","#"*11)
    print("-"*15, "HERO", "-"*15 )
    print(F"NAME: {hero_name}")
    print(F"HP: {hero_hp}")
    print(F"LIFE BAR [{"#"*hero_hp}{"-"*lost_hp}]")
          
    lost_hp = max_enemy_hp - enemy_hp
    print("-"*15, "ENEMY", "-"*14)
    print(F"NAME: {enemy_name}")
    print(F"HP: {enemy_hp}")
    print(F"LIFE BAR [{"#"*enemy_hp}{"-"*lost_hp}]")

def verify_winner(hero_hp, enemy_hp):
    if hero_hp <= 0 or enemy_hp <= 0:
        return True
    else:
        return False
        

#show_state("Neyder", 99, "Jeusu", 45)