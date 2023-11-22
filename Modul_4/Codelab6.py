def point(x, y):
    return x, y

def line_equation_of(p, M):
    C = p[1] - M * p[0]

    return f"y = {M:.2f}x + {C:.2f}"

# Example using the last three digits 093
print("Persamaan garis yang melalui titik (0,9) dan bergradien 3:")
print(line_equation_of(point(0, 9), 3))
