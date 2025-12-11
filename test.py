import os  # Unused import
import sys

def duplicated_code():
    print("Hello")  # Duplicate code
    print("Hello")

def complex_function(x):
    if x == 1:
        print("One")
    elif x == 2:
        print("Two")
    elif x == 3:
        print("Three")
    elif x == 4:
        print("Four")
    elif x == 5:
        print("Five")
    else:
        print("Other")

def potential_bug():
    x = "TEST"
    if x.lower() == "test":
        print("Bug!")

if __name__ == "__main__":
    unused_function()
    duplicated_code()
    complex_function(3)
    potential_bug()
