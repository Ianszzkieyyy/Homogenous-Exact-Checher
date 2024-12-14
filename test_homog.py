import sympy as sp

def TestHomogenous(function, name):
    x, y, λ = sp.symbols('x y λ')

    function_lambda = function.subs({
        x: λ * x,
        y: λ * y
    })

    function_lambda_simplified = sp.simplify(function_lambda)
    factored = sp.factor(function_lambda_simplified)

    try:
        coef, degree = factored.as_coeff_exponent(λ)
        return (name, function_lambda, function_lambda_simplified, factored, degree)
    
    except Exception as e:
        return None
