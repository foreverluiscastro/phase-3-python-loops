#!/usr/bin/env python3

def happy_new_year():
    # code goes here
    pass
    i = 10
    while i > 0:
        print(i)
        i -= 1

    print("Happy New Year!")

def square_integers(int_list):
    # code goes here
    pass
    square_list = list()
    for int in int_list:
        square = int * int
        square_list.append(square)
    return square_list

def fizzbuzz():
    # code goes here
    pass
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))
        i += 1

