def and_gate(a, b):

    if a == 1 and b == 1:

        return 1

    else:

        return 0

        

def not_gate(a):

    if a == 1:

        return 0

    else:

        return 1

        

def nand_gate(a, b):

    a = and_gate(a, b)

    return not_gate(a)

def or_gate(a, b):

    a = not_gate(a)

    b = not_gate(b)

    return nand_gate(a, b)

def xor_gate(a, b):

    c = nand_gate(a, b)

    d = nand_gate(not_gate(a), not_gate(b))

    return and_gate(c, d)

def half_adder(a, b):

    s = xor_gate(a, b)

    c = and_gate(a, b)

    return s, c

def full_adder(a, b, c_in):

    s1, c1 = half_adder(a, b)

    s2, c2 = half_adder(s1, c_in)

    c_out = or_gate(c1, c2)

    return s2, c_out

def one_bit_adder(a, b, c_in):

    s, c_out = full_adder(a, b, c_in)

    return s, c_out

def to_bin(n, num_bits):

    return bin(n)[2:].zfill(num_bits)

def from_bin(s):

    return int(s, 2)

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

        result = a - b

        print("Result:", result)

    elif op == '*':

        result = a * b

        print("Result:", result)

    elif op == '/':

        if b == 0:

            print("Error: division by zero")

            continue

        result = a / b

        print("Result:", result)

