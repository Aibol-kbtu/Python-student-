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

# Sample JSON data (you can use this or load from a file)
sample_json = '''
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


def parse_interface_data(json_string):
    """Parse JSON and display interface status in table format"""
    data = json.loads(json_string)

    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
    print("-" * 80)

    for interface in data['interface']:
        dn = interface['dn']
        description = interface['description'] or ' '
        speed = interface['speed']
        mtu = interface['mtu']

        print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")


# Run the function
parse_interface_data(sample_json)

import json

def read_from_file(filename='sample-data.json'):
    """Read and parse JSON data from file"""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return None

# Usage
data = read_from_file('sample-data.json')
if data:
    print("JSON data loaded successfully!")

import json
import os


def display_interface_status(filename='sample-data.json'):
    """Complete solution for displaying interface status from JSON file"""

    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return

    try:
        # Read and parse JSON file
        with open(filename, 'r') as file:
            data = json.load(file)

        # Display header
        print("Interface Status")
        print("=" * 80)
        print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
        print("-" * 80)

        # Display interface data
        for interface in data.get('interface', []):
            dn = interface.get('dn', 'N/A')
            description = interface.get('description', '') or ' '
            speed = interface.get('speed', 'N/A')
            mtu = interface.get('mtu', 'N/A')

            print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file")
    except KeyError as e:
        print(f"Error: Missing key in JSON data - {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Run the function
display_interface_status()

import json


def filter_interfaces(filename='sample-data.json', min_mtu=9000):
    """Filter interfaces based on MTU value"""

    with open(filename, 'r') as file:
        data = json.load(file)

    print(f"Interfaces with MTU >= {min_mtu}")
    print("=" * 60)
    print(f"{'DN':<40} {'MTU':<6}")
    print("-" * 60)

    filtered_count = 0
    for interface in data['interface']:
        mtu = int(interface['mtu'])
        if mtu >= min_mtu:
            print(f"{interface['dn']:<40} {mtu:<6}")
            filtered_count += 1

    print(f"\nTotal interfaces found: {filtered_count}")


# Usage
filter_interfaces()

import json
from collections import Counter


def analyze_interface_data(filename='sample-data.json'):
    """Analyze interface data and generate statistics"""

    with open(filename, 'r') as file:
        data = json.load(file)

    interfaces = data['interface']

    # Statistics
    total_interfaces = len(interfaces)
    speed_stats = Counter(interface['speed'] for interface in interfaces)
    mtu_values = [int(interface['mtu']) for interface in interfaces]

    print("Interface Data Analysis")
    print("=" * 30)
    print(f"Total interfaces: {total_interfaces}")
    print(f"\nSpeed distribution:")
    for speed, count in speed_stats.items():
        print(f"  {speed}: {count}")

    print(f"\nMTU Statistics:")
    print(f"  Minimum MTU: {min(mtu_values)}")
    print(f"  Maximum MTU: {max(mtu_values)}")
    print(f"  Average MTU: {sum(mtu_values) / len(mtu_values):.1f}")


# Usage
analyze_interface_data()