class StrManipulator:
    def __init__(value):
        value.string = ""

    def getstring(value):
        value.string = input(':')

    def printString(value):
        print(value.string.upper())

manipulator  = StrManipulator()
manipulator.getstring()
manipulator.printString()


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2



shape = Shape()
print(shape.area())
#для определения функциональности
#square = Square(5)
#print(square.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")

import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Point moved to: ({self.x}, {self.y})")

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance


# Test the class
point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()

print(f"Distance between points: {point1.dist(point2):.2f}")

point1.move(3, 5)
point1.show()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print(f"Insufficient funds! Available balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"


# Test the class
account = BankAccount("John Doe", 1000)
print(account)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.deposit(-100)
account.withdraw(-50)

def filter_primes_with_lambda(numbers):

    prime_check = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

    primes = filter(prime_check, numbers)

    return list(primes)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    print(filter_primes_with_lambda(numbers))

"""
------------------------------------------------------------------------------------------
"""
def grams_to_ounces(grams):
    return 28.3495231 * grams

grams = float(input("Введите вес в граммах: "))
ounces = grams_to_ounces(grams)
print(f"{grams} грамм = {ounces:.2f} унций")

'''
---------------------------------------------------------------------------------------------------------
'''
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

f_temp = float(input("Введите температуру в Фаренгейтах: "))
c_temp = fahrenheit_to_celsius(f_temp)
print(f"{f_temp}°F = {c_temp:.2f}°C")

"""
-------------------------------------------------------------------------
"""
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits

    if rabbits >= 0 and chickens >= 0 and rabbits.is_integer() and chickens.is_integer():
        return int(chickens), int(rabbits)
    else:
        return "No solve the problem"

chickens, rabbits = solve(35, 94)
print(f"Chickens: {chickens}, rabbits: {rabbits}")

"""
---------------------------------------------------------------------
"""
def filter_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    primes_regular = [x for x in numbers if filter_prime(x)]
    print(primes_regular)
"""
------------------------------------------------------------------------------------------
"""
recursive = input("Введите предложение: ")

words = recursive.split()
reversed_sentence = ' '.join(reversed(words))

print(reversed_sentence)
"""
---------------------------------------------------------------------------------------------
"""
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

"""
---------------------------------------------------------------------------------------------
"""
def spy_game(nums):
    p = [0, 0, 7]
    index = 0

    for num in nums:
        if num == p[index]:
            index += 1
            if index == len(p):
                return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
"""
---------------------------------------------------------------------------------------------
"""
import math
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

print(f"Volume of sphere with radius : {sphere_volume(5):.2f}")
"""
---------------------------------------------------------------------------------------------
"""
def unique_elements(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5, 1]
print(f"Original: {original_list}")
print(f"Unique: {unique_elements(original_list)}")
"""
---------------------------------------------------------------------------------------------
"""
def palindrome(word):
    cleaned = ''.join(word.split()).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    a = input("Enter a word or phrase: ")
    result = palindrome(a)
    if result:
        print("palindrom")
    else:
        print("Not palindrom")
"""
----------------------------------------------------------
"""
def histogram(numbers):
    for num in numbers:
        print('*' * num)

if __name__ == "__main__":
    test_data = [4, 9, 7]

    print("Horizontal histogram:")
    histogram(test_data)
"""
----------------------------------------------------------------
"""
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0

    while True:
        print("Take a guess.")
        try:
            guess = int(input())
            guesses_taken += 1

            if guess < number:
                print("Your guess is too low.")
            elif guess > number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
                break
        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    guess_the_number()
'''
-------------------------------------------------------------
'''
# Dictionary of movies
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# 1. Function that returns True if IMDB score is above 5.5
def is_high_rated(movie):
    return movie["imdb"] > 5.5


# 2. Function that returns sublist of movies with IMDB score above 5.5
def high_rated_movies(movies_list):
    return [movie for movie in movies_list if movie["imdb"] > 5.5]


# 3. Function that returns movies by category
def movies_by_category(movies_list, category):
    return [movie for movie in movies_list if movie["category"].lower() == category.lower()]


# 4. Function that computes average IMDB score for a list of movies
def average_imdb(movies_list):
    if not movies_list:
        return 0
    total_score = sum(movie["imdb"] for movie in movies_list)
    return total_score / len(movies_list)


# 5. Function that computes average IMDB score for a category
def category_average_imdb(movies_list, category):
    category_movies = movies_by_category(movies_list, category)
    return average_imdb(category_movies)


def demonstrate_movie_functions():
#1
    test_movie = movies[0]
    print(f"1. Is '{test_movie['name']}' highly rated? {is_high_rated(test_movie)}")

#2
    high_rated = high_rated_movies(movies)
    print(f"\n2. High rated movies (IMDB > 5.5): {len(high_rated)} movies")
    for movie in high_rated:
        print(f"   - {movie['name']}: {movie['imdb']}")

#3
    romance_movies = movies_by_category(movies, "Romance")
    print(f"\n3. Romance movies: {len(romance_movies)} movies")
    for movie in romance_movies:
        print(f"   - {movie['name']}: {movie['imdb']}")

#4
    avg_score = average_imdb(movies)
    print(f"\n4. Average IMDB score of all movies: {avg_score:.2f}")

#5
    romance_avg = category_average_imdb(movies, "Romance")
    print(f"5. Average IMDB score for Romance movies: {romance_avg:.2f}")


if __name__ == "__main__":
    demonstrate_movie_functions()