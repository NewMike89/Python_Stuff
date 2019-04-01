# Michael Schorr
# 3/21/19
# List of cubes for 1 - 10 with and without list comprehension.

# without list comprehension
cubes = []
for num in range(1, 11):
    cube = num**3
    cubes.append(cube)
print(cubes)
print("\n")

# with list comprehension
cubes2 = [nums**3 for nums in range(1, 11)]
print(cubes2)
