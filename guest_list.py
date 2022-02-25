# creating guest list
guest_list=['zigi', 'bigShaq', 'mummy','daddy','kenna','lenna','kah']
len(guest_list)
# message inviting my guests to the party
print(f"\n {guest_list[0].title()} you are invited at my dinner party")
print(f"\n {guest_list[1].title()} you are invited at my dinner party")
print(f"\n {guest_list[2].title()} you are invited at my dinner party")
print(f"\n {guest_list[3].title()} you are invited at my dinner party")
print(f"\n {guest_list[4].title()} you are invited at my dinner party")
print(f"\n {guest_list[5].title()} you are invited at my dinner party")
print(f"\n {guest_list[6].title()} you are invited at my dinner party")
# message saying one of  my guest can't make it to the party
print(f"\n {guest_list[0].title()} can't make it  to my dinner party")
del(guest_list[0])
# inserting a new guest 'grandma' into the list
guest_list.insert(0,'grandma')
print (guest_list)
# printing a new message to all my guests inviting them to the party
print(f"\n {guest_list[0].title()} you are invited at my dinner party")
print(f"\n {guest_list[1].title()} you are invited at my dinner party")
print(f" \n{guest_list[2].title()} you are invited at my dinner party")
print(f"\n {guest_list[3].title()} you are invited at my dinner party")
print(f"\n {guest_list[4].title()} you are invited at my dinner party")
print(f"\n {guest_list[5].title()} you are invited at my dinner party")
print(f"\n {guest_list[6].title()} you are invited at my dinner party")
# inviting 3 more new people into the party
print("\n Hey guys i found a bigger table")
guest_list.insert(2,'linda')
guest_list.insert(3,'ryan')
guest_list.insert(4,'payne')
print(guest_list)
# printing an invite to all the new guests
print(f"\n {guest_list[0].title()} you are invited at my dinner party")
print(f"\n {guest_list[1].title()} you are invited at my dinner party")
print(f"\n {guest_list[2].title()} you are invited at my dinner party")
print(f"\n {guest_list[3].title()} you are invited at my dinner party")
print(f"\n {guest_list[4].title()} you are invited at my dinner party")
print(f"\n {guest_list[5].title()} you are invited at my dinner party")
print(f"\n {guest_list[6].title()} you are invited at my dinner party")
print(f"\n {guest_list[7].title()} you are invited at my dinner party")
print(f"\n {guest_list[8].title()} you are invited at my dinner party")
print(f"\n {guest_list[9].title()} you are invited at my dinner party")

# removing all the guests so that only two of them remain
print("\n I am so sorry, I can only invite two people to dinner")
uninvited=guest_list.pop()
print(f"\nI am so sorry {uninvited.title()}, I can't invite you to dinner ")
uninvited=guest_list.pop()
print(f"\nI am so sorry {uninvited.title()}, I can't invite you to dinner ")
uninvited=guest_list.pop()
print(f"\nI am so sorry {uninvited.title()}, I can't invite you to dinner ")
uninvited=guest_list.pop()
print(f"\nI am so sorry {uninvited.title()}, I can't invite you to dinner ")
uninvited=guest_list.pop()
print(f"\nI am so sorry {uninvited.title()}, I can't invite you to dinner ")
uninvited=guest_list.pop()
print(f"\nI am so sorry {uninvited.title()}, I can't invite you to dinner ")
uninvited=guest_list.pop()
print(f"\nI am so sorry {uninvited.title()}, I can't invite you to dinner ")
uninvited=guest_list.pop()
print(f"\nI am so sorry {uninvited.title()}, I can't invite you to dinner ")
print(guest_list)
# deleting the remaining two guests so that the list remains empty as we started

del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)

print('Done')