from ast import If


my_foods=['achu','eru','koki','rice','banana','cake','stew']
friends_foods=my_foods[:]

print("my favourite foods are: ")
print(my_foods)

print("\n my friends favourite foods are: ")
print(friends_foods)

print("\n the first 3 items in the list are: ")
print(my_foods[0:3])

print("\n Three items from the middle of the list are ")
print(my_foods[2:5])

print("\n Three items from the end of the list are:")
print(my_foods[-3:])

for my_food in my_foods:
    print(my_food)
