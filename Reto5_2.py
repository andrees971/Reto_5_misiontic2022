import json
import  os

def registrarempleado():
    while True:
        try:
            id = int(input('Digite el No. de identificacion del empleado: '))
            if id in empleado.keys():
                print('Empleado ya existe')
            else:
                lista=[]
                lista.append(input('Nombre: '))
                lista.append(int(input('Digite el No. de Sucursal: ')))
                lista.append(int(input('Salario Base:')))
                lista.append(int(input('Dias Trabajados:')))
                empleado[id]= lista
            input('<ENTER> para continuar')
            break
        except ValueError:
            print('Error, no es valido. inetneta de nuevo...')
            

def mostrarInfoEmpleados():
    for i in empleado:
        print('[', i , '] ', empleado[i])
    input('<ENTER> para continuar')

def actualizarInformacion():
    try:
        buscar = int(input('Digite el No. de identificacion del empleado: '))    
        print(empleado[buscar])
        actualizar = input('Quiere actulizar la informacion (S/N):').upper()
        if(actualizar == 'S'):
            lista=[]
            lista.append(input('Nombre: '))
            lista.append(int(input('No. de Sucursal:')))
            lista.append(int(input('Salario Base:')))
            lista.append(int(input('Dias Trabajados:')))
            empleado[buscar]= lista
            print('Se Actualizo la informacion')
    except KeyError:
        print('El id a buscar no existe')
    except ValueError:
        print('valor digitado incorrecto')
    finally: 
        input('<ENTER> para continuar')

def eliminarEmpleado():
    buscar = int(input('Digite el No. de identificacion del empleado: '))
    print(empleado[buscar])
    eliminar = input('Quiere eliminar el empelado (S/N): ').upper()
    if(eliminar == 'S'):
        del(empleado[buscar])
        print('Empleado Eliminado')

def calcularPagoxDias(buscar):
    lista = empleado[buscar]
    sueldoMes = (lista[2]/30) * lista[3]
    return sueldoMes
        
def calcularAportesSSG(buscar):
    sueldoMes = calcularPagoxDias(buscar)
    ssg = sueldoMes * 0.08
    return ssg

def calcularAuxTrasporte(buscar):
    lista = empleado[buscar]
    auxTrasporte = (106454/30) * lista[3]
    return auxTrasporte


def calcularValorNeto():
    buscar = int(input('Digite el No. de identificacion del empleado: '))
    if buscar in empleado:
        lista = empleado[buscar]
        sueldoMes = calcularPagoxDias(buscar)
        ssg = calcularAportesSSG(buscar)
        auxTrasporte = calcularAuxTrasporte(buscar)

        valorNeto = sueldoMes - ssg + auxTrasporte
        print("ID: ", buscar)
        print("Nombre: ", lista[0])
        print("No. de surcursal: ",int(lista[1]))
        print("Salario basico: $", int(lista[2]))
        print("Dias trabajados: ", lista[3])
        print("Sueldo Mes: $", int(sueldoMes))
        print("Seguridad social: $", int(ssg))
        print("Auxilio de trasporte: $", int(auxTrasporte))
        print("Sueldo Neto: $", int(valorNeto))
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    else:
        print('Empleado no existe')

    input('<ENTER> para continuar')

def generarJSON():
    buscarSurcusal = int(input('Digite la sucursal de los empleados a listar: '))
    if buscarSurcusal > 0 and buscarSurcusal <=3:
        for i in empleado:
            lista = empleado[i]
            if(int(lista[1]) == buscarSurcusal):
                print(lista)
                sucursal[i] = lista
        
        with open('dato.json', 'w') as file:
            json.dump(sucursal, file, indent=4)
    else:
        print("Sucursal no existe...")
    input('<ENTER> para continuar')
    
def leerJSON():
    with open('dato.json') as file:

        for i in sucursal:
            print('[', i , '] ', sucursal[i])
    input('<ENTER> para continuar')


sucursal = {}

empleado = {
    15: ['Andres Silva', 1, 1000000, 30],
    16: ['Alejandra Torres', 1, 1000000, 23],
    17: ['Felipe Mu??oz', 2, 900000, 25],
    18: ['Estefani Cardona', 3, 950000, 15]
}



continuar = 'S'

while (continuar == 'S'):
    os.system('cls')

    print("MENU PRINCIPAL"
    + "\n 1.Registrar informacion"
    + "\n 2.Mostrar informacion"
    + "\n 3.Consultar y actulizar informacion de un empleado"
    + "\n 4.consultar y eliminar informacion de un empleado"
    + "\n 5.calcular la nomina"
    + "\n 6.Generar JSON"
    + "\n 7.Leer JSON"
    + "\n 8.Salir")
    op = int(input("Digite una opcion: "))

    
    if (op == 1):
        registrarempleado()
    elif (op == 2):
        mostrarInfoEmpleados()
    elif (op == 3):
        actualizarInformacion()
    elif (op == 4):
        try:
            eliminarEmpleado()
        except KeyError:
            print('El id digitado no existe..')
        except ValueError:
            print('valor digitado incorrecto') 
        finally:
            input('<ENTER> para continuar')
    elif (op == 5):
        calcularValorNeto()
    elif (op == 6):
        sucursal = {}
        generarJSON()
    elif (op == 7):
        leerJSON()
    elif (op == 8):
        continuar = 'N'
    else:
        print('opcion incorrecta')











