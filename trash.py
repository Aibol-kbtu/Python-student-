"""
Create a generator that generates the squares of numbers up to some number N.
"""
"""
def square(a):
    return a*a;

a = int(input(":"))
print(square(a))
"""
"""
Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
"""
"""
def even_numbers(n):
    arr = []
    for i in range(0,n+1):
        if i%2==0:
            return arr
    for i in range(len(arr)):
        return arr

b = int(input(": "))
print(even_numbers(b))
"""
"""
Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
"""
"""
def divisible(e):
    arr = []
    for i in range(0,e+1):
        if i%3==0 and i%4==0:
            arr.append(i)
    for i in range(len(arr)):
        return arr

s = int(input())
print(divisible(s))
"""
"""
Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
"""
"""
def yield_hash(a,b):
    arr =[]
    for i in range(a,b+1):
        arr.append(i)

    for i in range(len(arr)):
        return arr

a = int(input())

b = int(input())

print(yield_hash(a,b))
"""

"""
Implement a generator that returns all numbers from (n) down to 0.
"""
"""
def recursive(a):
    arr = []
    for i in range(a,-1,-1):
        arr.append(i)
    for i in range(len(arr)):
        return arr

a = int(input())
print(recursive(a))
"""
"""
Write a Python program to subtract five days from current date.
"""
"""
from datetime import date,timedelta
def time_five ():
    b = date.today()
    a = b + timedelta(days = 5)
    print(b)
    print(a)

time_five()
"""
"""
Write a Python program to print yesterday, today, tomorrow.
"""
"""
from datetime import date,timedelta
def date_fix():
    a = date.today()
    b = a + timedelta(days=-1)
    c = a + timedelta(days=1)
    print(b)
    print(a)
    print(c)

date_fix()
"""
"""
Write a Python program to drop microseconds from datetime.
"""
"""
import datetime
def micro_second():
    a = datetime.datetime.now()
    print(a.strftime("%f"))

micro_second()
"""
"""
Write a Python program to calculate two date difference in seconds.
"""
"""
from datetime import datetime
def second_mines():
    time1 = datetime(2024, 1, 15, 10, 30, 0)
    time2 = datetime(2024, 1, 15, 10, 45, 30)

    difference = (time1-time2).total_seconds()
    print(difference)

second_mines()
"""
"""
Write a Python program to convert degree to radian.
"""
"""
import math
def radian(a):
    return a * (math.pi/180)

a = float(input("input degree: "))
print(f"Output radian: {radian(a):.6f}")
"""
"""
Write a Python program to calculate the area of a trapezoid.
"""
"""
import math
def trapezoidal(a,b,c):
    return (a*(b+c))/2

a = int(input("Height: "))
b = int(input("Base, first value: "))
c = int(input("Base, second value: "))
print(f"Expected Output: {trapezoidal(a,b,c):.1f}")
"""
"""
Write a Python program to calculate the area of regular polygon.
"""
"""
import math
def polygon_area(b,c):
    a = c/2
    return (1/2)*(b*c*a)

a = int(input("Input number of sides: "))
b = int(input("Input the length of a side: "))

print(f"The area of the polygon is: {polygon_area(a,b):.0f}")
"""
"""
Write a Python program to calculate the area of a parallelogram.
"""
"""
def area_parallelogram(a,b):
    return a*b

a = int(input("Length of base: "))
b = int(input("Height of parallelogram: "))
print(f"Expected Output: {area_parallelogram(a,b):.1f}")
"""
import json

# JSON данные прямо в коде
json_data = '''
{
    "interface": [
        {
            "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
            "description": "",
            "speed": "inherit",
            "mtu": "9150"
        },
        {
            "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
            "description": "",
            "speed": "inherit",
            "mtu": "9150"
        },
        {
            "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]",
            "description": "",
            "speed": "inherit",
            "mtu": "9150"
        }
    ]
}
'''


def parse_from_string():
    data = json.loads(json_data)

    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
    print("-" * 80)

    for interface in data['interface']:
        print(
            f"{interface['dn']:<50} {interface['description'] or ' ':<20} {interface['speed']:<8} {interface['mtu']:<6}")



parse_from_string()