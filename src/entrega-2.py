import numpy as np
import matplotlib.pyplot as plt
import xlrd

def dot(unVec, otroVec):
   result = 0
   for j in range(121):
       result = result + (unVec[int(j)]*otroVec[int(j)])
   return result

book = xlrd.open_workbook('Entrega2.xlsx')
sheet = book.sheet_by_name('Sheet1')
cantDias = []
casos = []

for i in range(sheet.nrows):
    cantDias.append(sheet.cell_value(i, 3))
    casos.append(sheet.cell_value(i, 4))

plt.plot(cantDias, casos, 'ro')
plt.axis([0, 180, 0, 8000])
plt.show()

fises = []
fi0 = []
fi1 = []
fi2 = []
f = []

for i in range(121):
    fi0.append(float(1))

for i in range(121):
    fi1.append(float(i))

for i in range(121):
    iAlCuadrado = i**2
    fi2.append(float(iAlCuadrado))
for i in range(121):
    casosPorDia = (sheet.cell_value(i, 4))
    logaritmoDeCasos = np.log(casosPorDia)
    f.append(logaritmoDeCasos)

fises.append(fi0)
fises.append(fi1)
fises.append(fi2)

A = []
B = []
b = []
for i in range(3):
    A.append([])
    for j in range(3):
        value = np.dot(fises[i], fises[j])
        A[i].append(value)

B.append([])
B[0].append(float(dot(fi0, fi0)))
B[0].append(float(dot(fi0, fi1)))
B[0].append(float(dot(fi0, fi2)))
B.append([])
B[1].append(float(dot(fi1, fi0)))
B[1].append(float(dot(fi1, fi1)))
B[1].append(float(dot(fi1, fi2)))
B.append([])
B[2].append(float(dot(fi2, fi0)))
B[2].append(float(dot(fi2, fi1)))
B[2].append(float(dot(fi2, fi2)))

b.append(float(dot(f, fi0)))
b.append(float(dot(f, fi1)))
b.append(float(dot(f, fi2)))

x = np.linalg.solve(B, b)
print("B:  ", B)
print("A:  ", A)
print(x)
print(np.dot(A, x))
print((np.dot(A, x)) == b)




