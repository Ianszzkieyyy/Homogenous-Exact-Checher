import sympy as sp
import re

def EQParser(input_eq):

    input_eq = input_eq.replace(" ", "")

    if "dx" not in input_eq or "dy" not in input_eq or "=0" not in input_eq:
        print("Input equation must be in the format M(x,y)dx + N(x,y)dy = 0")
        return None
    
    try:
        match = re.match(r'^(.*?)dx([+-].*?)dy=0$', input_eq)
        
        if not match:
            print("Could not parse the equation. Ensure it's in M(x,y)dx + N(x,y)dy = 0 format")
            return None
        
        M_str = match.group(1)
        N_str = match.group(2)
        
        x, y = sp.symbols('x y')
        
        M = sp.parse_expr(M_str, transformations='all')
        N = sp.parse_expr(N_str, transformations='all')
        
        return (M, N)
    
    except Exception as e:
        print(f"Error parsing equation: {e}")
        return None

