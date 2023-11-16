#for loop
fruits = ["Apple", "Peach","Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

sum = 0

for number in range(1,101):
    sum += number

print(sum)



for number in range(1,11,3):
    print(number)

target = int(input("Give me an number dude!"))

even_sum = 0

for even in range(2,target+1,2):
    even_sum += even

print(even_sum)
