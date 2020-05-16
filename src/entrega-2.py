import numpy as np
import matplotlib.pyplot as plt
import  xlrd

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


