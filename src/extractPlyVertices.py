import os

x = []
y = []
z = []
with open("vertexTest.txt") as f:
    # skip first three lines
    for _ in range(3):
        next(f)
    # get the vertex count
    n = int(next(f).split()[-1])
    # skip next four lines
    for _ in range(4):
        next(f)
    # get the coordinate data
    for i in range(n):
        xi, yi, zi = map(float, next(f).split())
        x.append(xi)
        y.append(yi)
        z.append(zi)


x_min = min(x)
y_min = min(y)
z_min = min(z)

for i in range(n):
    x[i] -= x_min
    y[i] -= y_min
    z[i] -= z_min


abs_max = max(max(x), max(y), max(z))

for i in range(n):
    x[i] /= abs_max
    y[i] /= abs_max
    z[i] /= abs_max




with open("output.txt", "w") as outfile:
    outfile.write(f"{n}\n")
    for i in range(n):
        outfile.write(f"{x[i]} {y[i]} {z[i]}\n")
