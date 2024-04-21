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

# Example of using 
f_str = "2*x - sin(x) - 0.25 "
expr = string_to_expr(f_str)

# compute_derivative f(x)
f_prime = expr.diff()

# Create function from string
f_func = create_function_from_expr(expr)

# Create function from string derivative
f_prime_func = create_function_from_derivative(f_prime)

def newton_method(f, f_prime, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fpx = f_prime(x)
        if fpx == 0:
            return None
        x = x - fx / fpx
    return None

# Example of using
#x0 = 1.0  # First step
#solution = newton_method(f_func, f_prime_func, x0, 1e-6, 100)
#if solution is not None:
#    print(f"Solution: x = {solution}")
#else:
#    print("Solution wasn't found ")