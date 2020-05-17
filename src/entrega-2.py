import numpy as np
import matplotlib.pyplot as plt
import xlrd

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
    iAlCuadrado = -((i + 1) ** 2)
    fi0.append(iAlCuadrado)

for i in range(121):
    fi1.append(i+1)


for i in range(121):
    fi2.append(1)

for i in range(121):
    casosPorDia = (sheet.cell_value(i, 4))
    logaritmoDeCasos = np.log(casosPorDia)
    f.append(logaritmoDeCasos)

fises.append(fi0)
fises.append(fi1)
fises.append(fi2)

A = []
b = []

for i in range(3):
    A.append([])
    for j in range(3):
        value = np.dot(fises[i], fises[j])
        A[i].append(value)

for i in range(3):
    result = np.dot(f, fises[i])
    b.append(result)


x = []
x = np.linalg.solve(A,b)
print("\nObtenemos entonces:","\nCo:",x[0],"\nC1:",x[1],"\nC2:",x[2])


lista_f_estrella = []
for i in fi1:
    f_estrella = np.exp(x[2] + x[1] * float(i) - x[0] * (float(i) ** 2))
    lista_f_estrella.append(f_estrella)
for i in lista_f_estrella:  # valores
    print(i)



