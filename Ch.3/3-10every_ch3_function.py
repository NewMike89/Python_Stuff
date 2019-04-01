# Michael Schorr
# 3/13/19
# Program using every CH. 3 function at least once.

my_cars = ['toyota', 'audi', '818', 'slc']

# LEN()
print("the current list length is: " + str(len(my_cars)))
print("Here is that list of cars printed: ")
print(my_cars)

# APPEND()
my_cars.append('gtm')
print("I would really like to buy a " + my_cars[4].upper())
print("Here is the list in alphabetical order:")

# SORTED()
print(sorted(my_cars))
print("here it is again in reverse:")

# SORTED(REVERSE=TRUE)
print(sorted(my_cars, reverse=True))
print("And here in order from most expensive to least:")

# REVERSE()
my_cars.reverse()
print(my_cars)

# POP()
print("The " + my_cars.pop(4) + " is the only truck in the list")
too_old = 'audi'

# REMOVE()
my_cars.remove(too_old)
print("I removed another car from the list, can you figure out which one")
print(my_cars)
print("I will be buying the " + my_cars[-1] + " as my next car")

# DEL
del my_cars[0]
print("I got rid of my least favorite of the two most expensive cars")
print(my_cars)

# INSERT()
my_cars.insert(2, 'wrx')
print("I need to get a " + my_cars[2] + " to be able to build the " + my_cars[1])

# SORT()
my_cars.sort()
print("Here is the final list from A to Z so to speak")
print(my_cars)
print("Here is that list in reverse")

# SORT(REVERSE=TRUE)
my_cars.sort(reverse=True)
print(my_cars)
