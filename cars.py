# sorting list permanently with sort()
cars=['subaru','toyota','audi','bmw','volkswagen']
cars.sort()
print(cars)
cars=['subaru','toyota','audi','bmw','volkswagen']
cars.sort(reverse=True)
print(cars)
# sorting lists temporarily with the sorted() function
cars=['subaru','toyota','audi','bmw','volkswagen']
print("\nHere is the original list:")
print(cars)
print("\n Here is the temporarily sorted list:")
print(sorted(cars))
print("\n Here is the original list again:")
print(cars)
cars.reverse()
print(cars)