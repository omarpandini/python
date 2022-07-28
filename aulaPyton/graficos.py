from asyncore import loop
import matplotlib.pyplot as plt
import numpy

notas_matematica = [5, 6, 0, 8, 9, 9.5, 6.5, 8]

print( 'tamanho do array: '  + str(numpy.size(notas_matematica)))

array = []

for i in range(8):
    print(i+1)
    array.append(i+1)

y = notas_matematica

print(array)

plt.bar(array, y)
plt.show()
