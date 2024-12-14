import sympy as sp

def TestExact(M, N):

    x, y = sp.symbols('x y')
    isExact = None

    def partial_diff(function_of, variable):
        expression = sp.sympify(function_of)
        derivative = sp.diff(expression, variable)
        return derivative
    
    derivative_y_respect = partial_diff(M, y)
    derivative_x_respect = partial_diff(N, x)

    if derivative_y_respect == derivative_x_respect:
        isExact = True
    else:
        isExact = False

    return (derivative_y_respect, derivative_x_respect, isExact)
    