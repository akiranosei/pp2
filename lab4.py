#Python iterators and generators
#generate square of numbers up to some number N
def generate_squares(N):
    for i in range(1, N + 1):
        yield i ** 2
N = int(input("Enter a number: "))
for square in generate_squares(N):
    print(square, end=" ")

#generate even numbers between 0 and n
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number: "))
print(",".join(str(num) for num in even_numbers(n)))

#generate numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter number: "))
print("Numbers divisible by 3 and 4:")
for num in divisible_by_3_and_4(n):
    print(num, end=" ")

#generate squares yielding squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for sq in squares(a, b):
    print(sq)

#generate all numbers from n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input("Enter a number: "))
for num in countdown(n):
    print(num, end=" ")


#Python date
#substract five days from current date
from datetime import date, timedelta
current_date = date.today()
new_date = current_date - timedelta(days=5)
print("Current Date:", current_date)
print("Date 5 days ago:", new_date)

#print yesterday, today, tomorrow
from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#drop microseconds from datetime
from datetime import datetime
current_datetime = datetime.now()
without_microseconds = current_datetime.replace(microsecond=0)
print("With microseconds:", current_datetime)
print("Without microseconds:", without_microseconds)

#calculate two date difference in seconds
from datetime import datetime
date1 = datetime(2025, 10, 7, 12, 0, 0)
date2 = datetime(2025, 10, 9, 15, 30, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print(f"Difference between {date2} and {date1} is {seconds} seconds.")


#Python Math library
#convert degree to radian
import math
degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", round(radian, 6))

#calculate trapezoid area
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = ((base1 + base2) / 2) * height
print("Expected Output:", area)

#calculate regular polygon area
import math
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area, 2))

#calculate parallelogram area
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print("Expected Output:", area)


#Python JSON parsing
import json
with open("data.json") as f:
    data = json.load(f)
print("Interface Status")
print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print(f"{dn:50} {descr:20} {speed:8} {mtu:6}")




