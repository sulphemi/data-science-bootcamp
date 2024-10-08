# 1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
def count_vowels(word: str):
    return sum([ 1 for c in word.lower() if c in "aeiou" ]);

# 2. Iterate through the following list of animals and print each one in all caps.
for i in ['tiger', 'elephant', 'monkey', 'zebra', 'panther']:
    print(i.upper());

# 3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
for i in range(1, 20 + 1):
    print(f"{i} {'odd' if i & 1 else 'even'}");

# 4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
def sum_of_integers(a, b):
    return a + b;
