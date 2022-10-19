import math
x =[10, 10, 10]
y =[0, 0, -10]
v1 = math.sqrt(pow(int(x[0]), 2) + pow(int(x[1]), 2) + pow(int(x[2]), 2))
print(v1)
v2 = math.sqrt(pow(int(y[0]), 2) + pow(int(y[1]), 2) + pow(int(y[2]), 2))
print(v2)
v3 = math.sqrt(pow(v1, 2) + pow(v2, 2))
print(v3)