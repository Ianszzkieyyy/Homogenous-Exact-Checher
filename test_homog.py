import sympy as sp

def TestHomogenous(function, name):
    x, y, λ = sp.symbols('x y λ')

    function_lambda = function.subs({
        x: λ * x,
        y: λ * y
    })

    factored = sp.factor(function_lambda)
    factored_simplified = sp.simplify(factored)
    
    try:
        coef, degree = factored.as_coeff_exponent(λ)
        return (name, function_lambda, factored, factored_simplified, degree)
    
    except Exception as e:
        return None
