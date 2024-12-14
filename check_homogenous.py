import sympy as sp

def TestHomogenous(function, name):
    x, y, λ = sp.symbols('x y λ')

    print(f"Checking homogeneity for {name}(x, y): {function}")

    function_lambda = function.subs({
        x: λ * x,
        y: λ * y
    })
    print(f"After substituting x -> λx, y -> λy: {function_lambda}")

    function_lambda_simplified = sp.simplify(function_lambda)
    print(f"Simplified form of {name}(λx, λy): {function_lambda_simplified}")

    factored = sp.factor(function_lambda_simplified)
    print(f"Factored form: {factored}")

    try:
        coeff, degree = factored.as_coeff_exponent(λ)
        print(f"Degree with respect to λ: {degree}")

        if degree.is_number:
            print(f"{name}(x, y) is homogeneous of degree {degree}.")
            return degree
        else:
            print(f"{name}(x, y) is not homogeneous.")
            return None

    except Exception as e:
        print(f"Error during homogeneity check: {e}")
        return None
