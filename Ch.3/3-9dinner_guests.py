# Michael Schorr
# 3/13/19
# Adding a LEN() function to determine how many guests are in my list.

guests = ['george washington', 'bono', 'peter griffin']
print("Greetings Mr. " + guests[0].title() + ", I would like to invite you to dinner on the 1st of March.")
print(guests[1].title() + ". You, me, and two other blokes are goin out for some supper, March 1st. How bout it. YEAH YEAH YEAH!")
print("Hey there " + guests[2].title() + ". You want some food? Then get your butt down to my place on the 1st of March.")
print("There are " + str(len(guests)) + " guests in my list.")
