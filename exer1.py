square = lambda x: x ** 2
print(square(5))

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print("Carrés:", squared_numbers)
