# Michael Schorr
# 2/26/19
# Deletions from lists with DEL and POP()

# DEL
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# POP()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# POP() examples
motorcycles = ['honda', 'yamaha', 'suzuki']
last_onwed = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_onwed.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")
