from logic_gates import *

while True:

    op = input("Enter operation (+, -, *, /): ")

    if op not in ('+', '-', '*', '/'):

        print("Invalid operation")

        continue

    a = input("Enter first number: ")

    b = input("Enter second number: ")

    try:

        a = int(a)

        b = int(b)

    except ValueError:

        print("Invalid input")

        continue

    if op == '+':

        s, c_out = one_bit_adder(a & 1, b & 1, 0)

        result = s

        for i in range(1, 8):

            s, c_out = one_bit_adder((a >> i) & 1, (b >> i) & 1, c_out)

            result |= s << i

        print("Result:", result)

    elif op == '-':

        result = divider(subtractor(a, b)[0], 1)

        print("Result:", result)

    elif op == '*':

        result = multiplier(a, b)

        print("Result:", result)

    elif op == '/':

        try:

            result = divider(a, b)

            print("Result:", result)

        except ZeroDivisionError as e:

            print("Error:", str(e))

    quit = input("Quit? (y/n): ")

    if quit.lower() == 'y':

        break

