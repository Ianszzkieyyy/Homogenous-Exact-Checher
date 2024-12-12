import sympy as sp

x = sp.symbols('x')
y = sp.symbols('y')
lambda_symbol = sp.symbols('λ')


input_eq = input("Please enter equation: ")
# ex : (2x + y) dx + (x^2 + y)dy

def split_eq(input):
    M_str = ""
    N_str = ""
    sign = ''

    is_first = True
    is_second = False

    for index, chr in enumerate(input_eq):
        if chr == 'd':
            is_first = False
            is_second = False
            continue
        if (chr == 'x' or chr == 'y') and input_eq[index - 1] == 'd':
            continue
        if not is_first and not is_second and (chr == '+' or chr == '-'):
            sign = chr
            is_second = True
            continue
        if chr == '=':
            break

        if is_first:
            M_str += chr
        elif is_second:
            N_str += chr

    

    print(f"M: {M_str}, N: {N_str}, Sign: {sign}")



split_eq(input_eq)


        




