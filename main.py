import math
import sympy as sp
from sympy import solve
from sympy.utilities.lambdify import lambdify
import trapezoidalMethod


# Example when given the number of sections
x0 = 0
x1 = math.pi
num_sections = 4
x_ = sp.symbols('x')
func = sp.sin(x_)
func = lambdify(x_, func)
# print(f'Value of integral is {trapezoidalMethod.trapezoidal(func, x0, x1, num_sections):.4f}')


# Example when the number of sections is not given
# calculate the amount of the sections
x, y = sp.symbols('x y')
func_ = sp.sin(x)
f_prime1 = func_.diff(x)
f_prime2 = f_prime1.diff(x)
func_ = lambdify(x, func_)
f_prime2 = lambdify(x, f_prime2)
roots = solve(f_prime1, x)

array_max = []
for i in roots:
    if f_prime2(i) < 0:
        array_max.append(i)

max_ = array_max[0]
for j in array_max:
    if func_(j) > max_:
        max_ = j

error_range = 0.000002

# sections calculations
num_sections_accurate = trapezoidalMethod.calculate_amount_of_sections(func_(max_), x0, x1, error_range)
print(f'Value of integral is {trapezoidalMethod.trapezoidal(func, x0, x1, num_sections_accurate):.4f}')
