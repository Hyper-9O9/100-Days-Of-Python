########## Scope ##########

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies} ")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Local Scope
# It only exists in local functions

def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
# print(potion_strength)    <-- in this one we get error because it is local to a function only

# Global Scope
# Variables defined outside a function
# play health can be accessed inside and outside a function
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)
drink_potion()

# You can call a variale if it is in a block not a function
game_level = 3
enemies = ["skeleton", "zombie", "spider"]
if game_level < 5:
    new_enemy = enemies[0]
# you can print it with no error
print(new_enemy)
# But if we put the if block inside a function we will get an error because it is not accessable

# Modifying global variables


enemies = 1

def increase_enemies():
    # by using global <var name> we are saying we want to use the global variable called enemy
    global enemies
    enemies += 2
    print(f"Enemies inside function: {enemies} ")
# try as much as possible not to modify your global variable because you might cause errors in your code
# if you forget where the variable is or what it is
# but you can use it to read it that one is fine
increase_enemies()
print(f"Enemies outside function: {enemies}")

# A better way to do same as above instead of calling a global variable


enemies = 1

def increase_enemies():
    return enemies + 1
enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

# In python you cannot make constants the only thing you can do is just make the variable a caps as a reminder not to change

PI = 3.14
URL = "www.google.com"


