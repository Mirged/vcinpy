def not_gate(a):

    return int(not a)

def and_gate(a, b):

    return int(a and b)

def or_gate(a, b):

    return int(a or b)

def xor_gate(a, b):

    return int(a != b)

def half_adder(a, b):

    s = xor_gate(a, b)

    c_out = and_gate(a, b)

    return s, c_out

def full_adder(a, b, c_in):

    s1, c1 = half_adder(a, b)

    s2, c2 = half_adder(s1, c_in)

    c_out = or_gate(c1, c2)

    return s2, c_out

def one_bit_adder(a, b, c_in):

    s, c_out = full_adder(a, b, c_in)

    return s, c_out

def negator(n):

    return xor_gate(n, 0b11111111)

def subtractor(a, b):

    b = negator(b)

    s, c_out = one_bit_adder(a, b, 1)

    return s, c_out

def multiplier(a, b):

    if a == 0 or b == 0:

        return 0

    result = 0

    for i in range(8):

        if (b & 1) == 1:

            result = result + (a << i)

        b = b >> 1

    return result

def divider(a, b):

    if b == 0:

        raise ZeroDivisionError("division by zero")

    if a == 0:

        return 0

    result = 0

    remainder = 0

    for i in range(8):

        result = result << 1

        remainder = remainder << 1

        if (a & 0x80) == 0x80:

            remainder = remainder + 1

        a = a << 1

        if remainder >= b:

            remainder = subtractor(remainder, b)[0]

            result = result + 1

    return result

