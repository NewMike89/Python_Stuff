# Michael Schorr
# 4/3/19
# using 4-1 to crate a copy of the pizza list and add to it.

pizzas = ['buffalo chicken', 'zesty italian', 'pepperoni']
for pizza in pizzas:
    print(pizza.title() + ", is one of my favorite pizzas.")
print("I really like pizza, so much so that I ate a whole large pizza the other day at work. Everyone was very suprized that I was able to do so but I have to say. I LOVE PIZZA!!\n")

friend_pizzas = pizzas[:]

pizzas.append('loaded combo')
friend_pizzas.append('blue cheese ranch')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza.title())
print("\nMy friends favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
