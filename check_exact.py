import sympy as sp


def TestExact(M, N):
    x, y = sp.symbols('x y')

    def partial_diff(function_of, variable):
        expression = sp.sympify(function_of)
        derivative = sp.diff(expression, variable)
        return derivative

    derivative_y_respect = partial_diff(M, y)
    print(f"The partial derivative of {M} with respect to y is: {derivative_y_respect}")

    derivative_x_respect = partial_diff(N, x)
    print(f"The partial derivative of {N} with respect to x is: {derivative_x_respect}")

    if derivative_y_respect == derivative_x_respect:
        print("Your input is exact.")
    else:
        print("Your input is not exact.")

