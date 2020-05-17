import numpy as np
import matplotlib.pyplot as plt
import xlrd

def dot(unVec, otroVec):
   result = 0
   for j in range(65):
       result = result + (unVec[int(j)]*otroVec[int(j)])
   return result

book = xlrd.open_workbook('Entrega2.xlsx')
sheet = book.sheet_by_name('Sheet1')
cantDias = []
casos = []

for i in range(sheet.nrows):
    cantDias.append(sheet.cell_value(i, 9))
    casos.append(sheet.cell_value(i, 10))

plt.plot(cantDias, casos, 'ro')
plt.axis([0, 180, 0, 8000])
plt.show()

fises = []
fi0 = []
fi1 = []
fi2 = []
f = []

for i in range(65):
    fi0.append(float(1))

for i in range(65):
    fi1.append(float(i))

for i in range(65):
    iAlCuadrado = i**2
    fi2.append(float(iAlCuadrado))
for i in range(65):
    casosPorDia = (sheet.cell_value(i, 10))
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
print("A:  ", B)
print("b:  ", b)
print("b:  ", np.dot(A, x))
print("x:  ", x)
print("C0:", x[0], "C1:", x[1], "C2:", x[2])
print((np.dot(B, x)) == b)

for i in range(65):
    exponente = 1.4296830292159304 + (i+1)*0.3463955576491053 - ((i+1)**2)*0.004224080337535776
    print(np.exp(exponente))




