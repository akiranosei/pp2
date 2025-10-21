#Python builtin function excercises
#Multiply all numbers in one list
numbers=[1,2,3,4,5,6,7,8,9,10]
def multiply(i):
    return eval('*'.join(map(str, i)))
print(multiply(numbers))

#Calculate all uppercase and lowcaseletters
string = "AbbAbbAaaBBaab"
uppercase=0
lowercase=0
for l in string:
    if l.isupper():
        uppercase+=1
    elif l.islower():
        lowercase+=1
print(f"Uppercase letters: {uppercase}", f"Lowercase letters: {lowercase}")

#Check if palindrome or not
string = "abba"
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome(string))

#Invoke square root function after specific milliseconds
import time
x = 25100
delay = 2123
time.sleep(delay / 1000)
sqrt=pow(x,0.5)
print(f"Square root of {x} after {delay} milliseconds is {sqrt}")

#Return True if all elements of tuple are true
tuple = ("Hello World", True, False, 1, 2, 3)
print( all(tuple))


#Python Directories and Files exercises
#List only directories, files and all directories, files in a specified path
import os
path = 'C:/Users/User/AppData/Local/Programs/Python/Python312'
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print("Directories:", dirs)
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("Files:", files)
all_items = os.listdir(path)
print("All items:", all_items)

#Check for access for specified path, test existence, readability, writability, executability of that path
import os
path = 'C:/Users/User/AppData/Local/Programs/Python/Python312/python.exe'
print("Exists:", os.path.exists(path))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

#Test if path exists or not. If yes, print name and dorectory portion of that path
import os
path = 'C:/Users/User/AppData/Local/Programs/Python/Python312/python.exe'
if os.path.exists(path):
    print("Path exists")
    print(f"Filename: {os.path.basename(path)}",f"Directory: {os.path.dirname(path)}")
else:
    print("Path does not exist")

#Count number of lines in the file
with open('C:/Users/User/Downloads/newfile.txt', 'r') as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

#Write list to file
lines_to_write = ['line1\n', 'line2\n', 'line3\n']
with open('C:/Users/User/Downloads/newfile.txt', 'w') as file:
    file.writelines(lines_to_write)

#Generate 26 text files named A.txt, B.txt till Z.txt
for c in range(ord('A'), ord('Z') + 1):
    filename = chr(c) + '.txt'
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")

#Copy contents of one file to another
with open('newfile.txt', 'r') as src, open('output.txt', 'w') as dest:
    content = src.read()
    dest.write(content)

#Delete file by specified path, before check access and if exists or not
import os
file_path = 'C:/Users/User/Downloads/newfile.txt'
if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print(f"{file_path} deleted.")
else:
    print(f"File does not exist or can't be accessed: {file_path}")
