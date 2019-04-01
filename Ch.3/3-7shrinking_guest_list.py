# Michael Schorr
# 2/28/19
# creating a list of anyone I want and inviting them to dinner on my new large dinner table.

guests = ['george washington', 'bono', 'peter griffin']
message = ", Hey would you like to come to dinner on the 1st of March"
print("Hey everyone I just bought a large new dinner table.")
guests.insert(0, 'chuck norris')
guests.insert(2, 'the preditor')
guests.append('bibble from mars')
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)
print(guests[3].title() + message)
print(guests[4].title() + message)
print(guests[5].title() + message)
print("Bad news everyone, found out that the dinner table won't be delivered in time. So I only have room for two peole now.")
msg2 = ", sorry you have been cut from the dinner party"
cut_list = guests.pop(0)
print(cut_list.title() + msg2)
cut_list = guests.pop(0)
print(cut_list.title() + msg2)
cut_list = guests.pop(0)
print(cut_list.title() + msg2)
cut_list = guests.pop(0)
print(cut_list.title() + msg2)
msg3 = ", Congrats you are still coming to the party"
print(guests[0].title() + msg3)
print(guests[1].title() + msg3)
del guests[0]
del guests[0]
print(guests)
