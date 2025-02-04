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
