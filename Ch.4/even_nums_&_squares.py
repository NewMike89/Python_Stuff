# Michael Schorr
# 3/20/19
# using RANGE() to provide just the even numbers in a list.

even_nums = list(range(2, 11, 2))
print(even_nums)

# finding the square of 1-10 with FOR & RANGE() to create a list.

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# same list but with list comprehension.

squares = [value**2 for value in range(1, 11)]
print(squares)
