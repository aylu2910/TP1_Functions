'''def realizarPatron(cant_filas):
    i = 1
    for i in range(1,cant_filas+1):
        print(10*"*","                                     ",2*i*"*")'''

def columna_uno(cant_filas):
    i = 1
    for i in range(1,cant_filas+1):
        return 10*"*","                                     "
        
def columna_dos(cant_filas):
    i = 1
    for i in range(1,cant_filas+1):
        return 2*i*"*"
        
#PROGRAMA PRINCIPAL
filas = int(input("Ingrese cantidad de filas: "))
print(columna_uno(filas) + columna_dos(filas))