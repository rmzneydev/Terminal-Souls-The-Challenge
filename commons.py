import random
def generate_damage(min:int, max:int):
    damage = random.randint(min, max)
    return damage

def show_state(hero_name: str, hero_hp:int, enemy_name:str, enemy_hp:int):
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

def verify_winner(hero_hp:int, enemy_hp:int):
    if hero_hp <= 0 or enemy_hp <= 0:
        return True
    else:
        return False
        
def critical_system(damage: int):
    probability = random.randint(1,100)
    if probability <=10:
        damage = damage * 2
    return damage