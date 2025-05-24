from scipy.integrate import quad

b = 4 
h = 3 
def triangle_height(x):
    if x <= b / 2:
        return (2 * h / b) * x
    else:
        return (-2 * h / b) * x + 2 * h
area = quad(triangle_height, 0, b)

print(f"Area under the triangle: {area}")
