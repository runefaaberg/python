import random
import my_module

random_integer = random.randint(0,5)
print(random_integer)
#print(my_module.pi)

random_float = random.random()
print(random_float)

print(random_float*random_integer)

love_score = random.randint(1,100)

print(f"Your love score is {love_score}.")