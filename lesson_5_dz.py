#задание про рулетку
import numpy as np
myli =[1, 3,5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
for i in range(0, 5):
    x = np.random.randint(0, 36)

    if x in myli:

        print(x, 'red')

    elif x == 0:
        print( 'zero')
    else:
        print( x, 'green')


#Сгенерируйте десять выборок случайных чисел х0, …, х9.
#и постройте гистограмму распределения случайной суммы  +х0+ …+ х 9.

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

x = []
for i in range(0, 10):
    y = np.random.randint(0, 100)
    x.append(y)

a = sum(x)
num_bins = 3
n, bins, patches = plt.hist(a, num_bins)
plt.xlabel('sum')
plt.ylabel('Probabilyty')
plt.title('Histogram')
plt.show()
