
import sympy
def string_to_expr(f_str):
    x = sympy.Symbol('x')
    f = sympy.sympify(f_str)
    return f

def create_function_from_expr(expr):
    x = sympy.Symbol('x')
    f = sympy.lambdify(x, expr)
    return f

def create_function_from_derivative(derivative):
    x = sympy.Symbol('x')
    f = sympy.lambdify(x, derivative)
    return f