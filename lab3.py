#Python Classes
#1
class String:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#4
import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, one_point):
        return math.sqrt((self.x - one_point.x) ** 2 + (self.y - one_point.y) ** 2)

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount} and New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal can't be done! Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal: {amount} and New Balance: {self.balance}")

#6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)

#Python Function p.1
#1
def grams_to_ounces(grams):
    return 28.3495231 * grams
print(grams_to_ounces())

#2
def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)
print(fahrenheit_to_celsius())

#3
def solve(numheads, numlegs):
    for a in range(numheads + 1):
        b = numheads - a
        if 2*b + 4*a == numlegs:
            return b, a
    return None
print(solve())

#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]
print(filter_prime())

#5
import itertools

def string_permutations(s):
    perms = itertools.permutations(s)
    for p in perms:
        print(''.join(p))
string_permutations()

#6
def reverse_sentence(s):
    words = s.split()
    return ' '.join(words[::-1])
print(reverse_sentence())

#7
def has_33(nums):
    for i in range(len(nums) - 1):  # loop until second-last index
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
has_33([1, 3, 3]) #→ True
has_33([1, 3, 1, 3]) #→ False
has_33([3, 1, 3]) #→ False

#8
def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    
    for n in nums:
        if n == code[index]:
            index += 1
        if index == len(code):
            return True
    return False
spy_game([1,2,4,0,0,7,5]) #--> True
spy_game([1,0,2,4,0,5,7]) #--> True
spy_game([1,7,2,0,4,5,0]) #--> False

#9
import math
def sphere_volume(r):
    return (4/3) * math.pi * (r ** 3)
print(sphere_volume())

#10
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique
print(unique_list())

#11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome())

#12
def histogram(lst):
    for num in lst:
        print('*' * num)
histogram()

#13
import random
def guess_number_game():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1

        if guess < number:
            print("Your guess is too low.\n")
        elif guess > number:
            print("Your guess is too high.\n")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
guess_number_game()

#Python Function p.2
#1
def is_high_score(movie):
    return movie["imdb"] > 5.5
print(is_high_score())

#2
def high_score_movies(movie_list):
    return [m for m in movie_list if m["imdb"] > 5.5]
print(high_score_movies())

#3
def movies_by_category(movie_list, category):
    return [m for m in movie_list if m["category"] == category]
print(movies_by_category())

#4
def average_imdb(movie_list):
    if not movie_list:
        return 0
    return sum(m["imdb"] for m in movie_list) / len(movie_list)
print(average_imdb())

#5
def average_imdb_by_category(movie_list, category):
    filtered = [m for m in movie_list if m["category"] == category]
    return average_imdb(filtered)
print(average_imdb_by_category())







