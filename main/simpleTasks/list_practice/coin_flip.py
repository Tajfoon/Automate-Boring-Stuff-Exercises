import random

num_flips = 100
one_row = 10
list_results = []
howMany_O = 0
howMany_R = 0

# Drawing the results of the coin flip:
for x in range(num_flips):
    column = []
    for y in range(one_row):
        if random.randint(0, 1) == 0:
            column.append('O')
        else:
            column.append('R')
    list_results.append(column)


for row in list_results:
    print(row, end='\n')
    for cell in row:
        if cell == 'O':
            howMany_O += 1
        else:
            howMany_R += 1

print(f"You throw eagle: {howMany_O} times")
print(f"You throw headstock: {howMany_R} times")

total_flips = howMany_O + howMany_R
prec_O = (howMany_O / total_flips) * 100
prec_R = (howMany_R / total_flips) * 100

print(f"The precentage result of the total throws is {round(prec_O)}% eagle and {round(prec_R)}% headstock. ")