from ast import If
from socket import if_indextoname


motocycles=['honda','yamaha','suzuki','kawazaki']
print(motocycles)
popped_motocycle=motocycles.pop()
print(motocycles)
print(popped_motocycle)
last_owned=motocycles.pop(1)
print(f"the 2nd motocycle I owned was a {last_owned.title()} ")
print(motocycles)
motocycles.remove('honda')
too_expensive='honda'
print(f'\n A {too_expensive.title()} is too expensive for me ')
print(motocycles)
