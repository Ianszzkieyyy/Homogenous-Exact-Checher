import sympy as sp

def EQParser(input):

    x, y = sp.symbols('x y')

    input_eq = input_eq.replace(" ", "")
    
    if "dx" in input_eq and "dy" in input_eq:
        parts = input_eq.split("dx")  # Split at 'dx'
        M_str = parts[0].strip("()+")  # Before 'dx' is M
        N_str = parts[1].split("dy")[0].strip("()+")  # Between 'dx' and 'dy' is N

        print(M_str, N_str)
        
        try:
            M = sp.parse_expr(M_str, transformations='all')
            N = sp.parse_expr(N_str, transformations='all')
            print("M =")
            sp.pprint(M)
            print("N =")
            sp.pprint(N)
        except Exception as e:
            print("Error in sympifying M or N:", e)
    else:
        print("Input equation is not in the format M(x,y)dx + N(x,y)dy = 0.")
