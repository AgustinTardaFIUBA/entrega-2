import math
import numpy
import csv


def formando_funcion(fi,xi):
    contador = 0
    yi = []
    funcion_2 = []
    funcion_1 = []
    funcion_3 = []
    for i in fi:
        yi.append(math.log(int(i)))
    for i in xi:
        funcion_2.append(float(i))
        contador += 1
    for i in range(contador):
        funcion_1.append(1)
    for i in funcion_2:
        funcion_3.append(float(i)**2)
    return funcion_1,funcion_2,funcion_3,yi
    
def producto_interno(funcion_1,funcion_2,funcion_3,yi):
    lista_matriz = []
    b = []
    producto_interno1 = numpy.dot(funcion_1,funcion_1)
    producto_interno2 = numpy.dot(funcion_1,funcion_2) #mismo que el numpy.dot(funcion_2,funcion_1)
    producto_interno3 = numpy.dot(funcion_1,funcion_3) #mismo que el numpy.dot(funcion_3,funcion_1)
    producto_interno4 = numpy.dot(funcion_2,funcion_2)
    producto_interno5 = numpy.dot(funcion_2,funcion_3) #mismo que el numpy.dot(funcion_3,funcion_2)
    producto_interno6 = numpy.dot(funcion_3,funcion_3)
    producto_interno_f1 = numpy.dot(yi,funcion_1)
    producto_interno_f2 = numpy.dot(yi,funcion_2)
    producto_interno_f3 = numpy.dot(yi,funcion_3)
    print("\n(f0,f0):",producto_interno1,"\n(f0,f1):",producto_interno2,"\n(f0,f2):",producto_interno3,"\n(f1,f1):",producto_interno4,"\n(f1,f2):",producto_interno5,"\n(f2,f2):",producto_interno6,"\n(yi,f0):",producto_interno_f1,"\n(yi,f1):",producto_interno_f2,"\n(yi,f2):",producto_interno_f3)
    lista_matriz.append(producto_interno1)
    lista_matriz.append(producto_interno2)
    lista_matriz.append(producto_interno3)
    lista_matriz.append(producto_interno4)
    lista_matriz.append(producto_interno5)
    lista_matriz.append(producto_interno6)
    b.append(producto_interno_f1)
    b.append(producto_interno_f2)
    b.append(producto_interno_f3)
    return lista_matriz,b
 
def generar_matriz(lista_matriz):
    vec1 = []
    vec2 = []
    vec3 = []
    A = []
    vec1.append(lista_matriz[0])
    vec1.append(lista_matriz[1])
    vec1.append(lista_matriz[2])
    vec2.append(lista_matriz[1])
    vec2.append(lista_matriz[3])
    vec2.append(lista_matriz[4])
    vec3.append(lista_matriz[2])
    vec3.append(lista_matriz[4])
    vec3.append(lista_matriz[5])
    A.append(vec1)
    A.append(vec2)
    A.append(vec3)
    print("\nMatriz A:",A)
    return A
    
def calculo_cuadrados_minimos(A,b):
    print("\nVector b:",b)
    x = []
    x = numpy.linalg.solve(A,b)
    print("\nObtenemos entonces:","\nCo:",x[0],"\nC1:",x[1],"\nC2:",x[2])
    return x

def calculo_error_global(x,funcion_2,fi):
    e = []
    error = 0
    f_estrella = 0
    lista_f_estrella = []
    norma_error = 0
    norma_funcion = 0
    error_relativo = 0
    for i in funcion_2:
        f_estrella = numpy.exp(x[0] + x[1]*float(i) + x[2] * (float(i)**2))
        lista_f_estrella.append(f_estrella)
    for i in lista_f_estrella:          #valores
        print(i)
    for i in range(len(lista_f_estrella)):
        error = float(lista_f_estrella[i]) - float(fi[i])
        e.append(error)
    norma_error = numpy.linalg.norm(e)
    norma_funcion = numpy.linalg.norm(fi)
    error_relativo = norma_error/norma_funcion
    print("\nEl error relativo que obtuvimos aproximando la funcion fi(xi) con fi*(xi) es:",error_relativo)
    

def main():
    print("Sea f*(x)=yi=exp(Co + C1*zi + C2*(zi**2))","\nCalculamos los productos internos para poder formar el sistema Ax = b")
    fi = []
    xi = []
    yi = []
    funcion_2 = []
    funcion_1 = []
    funcion_3 = []
    lista_matriz = []
    b = []
    A = []
    x = []

    with open("tabNuevo.csv","r") as archivo:
        for linea in archivo:
            linea = linea.rstrip("\n").split(",")
            fi.append(linea[2])
            xi.append(linea[1])
    funcion_1,funcion_2,funcion_3,yi = formando_funcion(fi,xi)
    lista_matriz,b = producto_interno(funcion_1,funcion_2,funcion_3,yi)
    A = generar_matriz(lista_matriz)
    x = calculo_cuadrados_minimos(A,b)
    calculo_error_global(x,funcion_2,fi)
        
main()
        
    
        


    

            
        
            
    
    
    
    