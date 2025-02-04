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
filtered_words = list(filter(lambda word: word.startswith("a"), words))
print("Mots commençant par 'a':", filtered_words)

def count_long_words():
    count = 0
    def counter(word):
        nonlocal count
        if len(word) > 5:
            count += 1
        return count
    return counter

word_counter = count_long_words()
for word in words:
    word_counter(word)
print("Nombre de mots > 5 caractères:", word_counter("") )

#Exercice 5:
def compose(f, g):
    return lambda x: f(g(x))

f1 = lambda x: x + 2
f2 = lambda x: x * 3
composed_function = compose(f1, f2)
print("Composée:", composed_function(4))

#Exercice 6:
def filterMap(filter_func, map_func, lst):
    return [map_func(x) for x in lst if filter_func(x)]

words = ["", "hello", "world", "python", ""]
result = filterMap(lambda x: x != "", lambda x:
x.upper(), words)
print(result) # ['HELLO', 'WORLD', 'PYTHON']

#Exercice 7:
def memoize(f):
    cache = {}
    def memoized_function(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return memoized_function

@memoize
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

@memoize
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

print("Factorielle de 5:", factorial(5))
print("Fibonacci de 10:", fibonacci(10))


#Exercice 8:
def calculateDiscount(products, discount_func):
    return sum(discount_func(price) for price in products)

products = [100, 200, 300, 400]
discount_20 = lambda price: price * 0.8

totaldiscount = calculateDiscount(products, discount_20)
print("Total discount:", totaldiscount)