# Michael Schorr
# 4/3/19
# Making a copy of a list and that the copy can be modified. Then creating some loops to print each item individually.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')


print("My favorite foods are:")
# oringal print: print(my_foods)
# new print:
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
# oringal print: print(friend_foods)
# new print:
for friend_food in friend_foods:
    print(friend_food.title())
