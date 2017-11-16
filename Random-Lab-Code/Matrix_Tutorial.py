import numpy as np

a = np.matrix('2 4 ; 1 5')
b = np.matrix('1 4 ; -2 3')

print(a*b, '\n')

c = np.matrix('3 2 ; -1 0')

w, v = np.linalg.eig(c)

print('Lambda: \n', w)
print('\nVector: \n', v)