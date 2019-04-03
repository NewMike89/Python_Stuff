# Michael Schorr
# 4/3/19
# using PLAYERS.PY to print some lines with certain sections of the list

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

print("Here are the first three players in the list: ")
for player in players[:3]:
    print(player.title())

print("Here are the three players in the middle of the list: ")
for player in players[1:4]:
    print(player.title())

print("Here are the three players from the end of the list: ")
for player in players[-3:]:
    print(player.title())
