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

