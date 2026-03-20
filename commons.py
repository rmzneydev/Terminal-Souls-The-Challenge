import random
def generate_damage(min:int, max:int):
    damage = random.randint(min, max)
    return damage

def show_state(hero_name: str, hero_hp:int, enemy_name:str, enemy_hp:int, potions:int):
    max_hero_hp = 100
    max_enemy_hp = 120
    
    lost_hp = max_hero_hp - hero_hp
    print("╔"+"═"*60, "GAME STATUS","═"*60+"╗")
    print(" > HERO")
    print(f"   NAME: {hero_name}")
    print(f"   HP: {hero_hp}/{max_hero_hp}")
    print(f"   Potions: {potions}")
    print(f"   LIFE [{"█"*hero_hp}{"░"*lost_hp}]")
    print("═"*135)
    lost_hp = max_enemy_hp - enemy_hp
    print(" > ENEMY")
    print(f"   NAME: {enemy_name}")
    print(f"   HP: {enemy_hp}/{max_enemy_hp}")
    print(f"   LIFE [{"█"*enemy_hp}{"░"*lost_hp}]")
    print("╚"+"═"*134+"╝")
        


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
