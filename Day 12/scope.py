# constant uppercase
PI = 3.14159

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside the function {enemies}")

enemies = 1

# def increase_enemies():
#      global enemies
#      enemies += 1
#      print(f"enemies inside the function {enemies}")

def increase_enemies():
    print(f"enemies inside the function {enemies}")    
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside the function {enemies}")

#local scope

def drink_potion():
    potion_strength = 2
    print(player_health)

#drink_potion()
#print(potion_strength)

#global scope
player_health = 10

drink_potion()

#there is no block scope
game_level = 3
def create_ememy():
    enemies = ["Skeleton", "Zombie", "Alien"]

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

PI = 3

print(PI)