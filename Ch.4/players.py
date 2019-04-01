# Michael Schorr
# 4/1/19
# slicing a list, to select specific group from within it.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# displays from the first index to the one before the last listed index
print(players[0:3])
print(players[1:4])
# displays from the beginning of the list to the one before the last listed index
print(players[:4])
# displays from the first listed index to the end of the listed
print(players[2:])
# displays the number of items from the end of the list
print(players[-3:])


# Looping through a slice

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
