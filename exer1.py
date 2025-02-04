#Exercice 1:
from functools import reduce

square = lambda x: x ** 2
print(square(5))

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print("Carrés:", squared_numbers)

sum_two = lambda a, b: a + b
print(sum_two(3, 4))

total_sum = reduce(sum_two, numbers)
print("Somme totale:", total_sum)

#Exercice 2:
def create_multiplier(n):
    return lambda x: x * n

double = create_multiplier(2)
triple = create_multiplier(3)

print("Double de 4:", double(4))
print("Triple de 4:", triple(4))

#Exercice 3:
words = ["apple", "banana", "avocado", "cherry", "apricot", "grape"]
