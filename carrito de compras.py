"""
Ejercicios finales
Eduardo Garcia Castrejón
Fisica 1A
Programa 4
LISTA DE COMPRAS
"""

import string

#agregar al carito
def agregar(case):
    case = variableCase(case)
    if case != 0:
        carrito.append(productos[case - 1])
        pagar.append(precios[case - 1])
        print("Se ha agregado el poducto {0} ({1}) al carrito".format(case,productos[case - 1]))
        return agregar(case)

#Ver carrito
def verCarrito(q):
    q = []
    for i in range(0,len(carrito)):
        n = productos.index(carrito[i])
        m = carrito.count(carrito[i])
        p = ("{0}. {1} - ${2} - Cantidad:{3}".format(n+1,carrito[i],precios[n] * m,m))
        if p not in q:
            q.append(p)
    q.sort()
    print("\n".join(q))
    input("Enter para Continuar")

#Eliminar Carrito
def eliminarCarrito(Delete):
    verCarrito(q)
    Delete = variableDelete(Delete)
    if Delete != 0:
        if productos[Delete - 1] in carrito:
            print("Se ha eliminado un poducto: {0} ({1}) del carrito\n".format(Delete,productos[Delete - 1]))
            carrito.remove(productos[Delete - 1])
            pagar.remove(precios[Delete - 1])
        elif productos[Delete - 1] not in carrito:
            print("Ese producto no está en tu carrito\n")
        if len(carrito) == 0:
            print("\nHas vaciado tu carrito. Regreso al Menú")
        else:
            return eliminarCarrito(Delete)

#Pagar
def cajero(pagar):
    suma = 0
    coin = 0
    for x in pagar:
        suma += x
    print("Total a pagar: ",suma,)
    while suma != 0:
        coin = variableCoin(coin)
        suma -= coin
        if suma <= -1:
            print("Recibo {0} pesos. Cambio: ${1}".format(coin,suma * -1))
            suma = 0
        if suma > 0:
            print("Te falta pagar: {0} pesos".format(suma))
    print("\n¡Compra realizada con éxito!")

#menu
def menu():
    print("\nMenu")
    print("1. Comprar productos")
    print("2. Ver carrito")
    print("3. Eliminar elementos del carrito")
    print("4. Pagar")
    print("5. Salir\n")

#función para limitar variable opc
def variableMenu(opc):
    while True:
        opc = input("Introduce número: ")
        if len(opc) != 1 or opc not in '12345':
            print("Favor de introducir numero entre 1 y 5: ")
        else:
            return int(opc)

#función para limitar variable case
def variableCase(case):
    while True:
        case = input("Agrega producto al carrito: (o regresa) ")
        if len(case) != 1 or case not in '01234567':
            print("Favor de introducir numero entre 0 y 7: ")
        else:
            return int(case)

#función para limitar variable Delete
def variableDelete(Delete):
    while True:
        Delete = input("\nElimina algún producto del carrito: (o regresa con '0') ")
        if Delete not in string.digits or len(Delete) >= 2:
            print("Favor de introducir solo números de dos digitos")
        else:
            return int(Delete)

#función para limitar variable coin
def variableCoin(coin):
    while True:
        coin = input("Ingresa una moneda ($1,$5,$10): ")
        if coin not in '105':
            print("Favor de introducir monedas de 1,5 y 10: ")
        else:
            return int(coin)

#Mostrar lista de productos
def producto(productos,precios):
    print(" ")
    for i in range(0,len(productos)):
        print("{0}. {1} - ${2}".format(i+1,productos[i],precios[i]))
    print("0. Regresar Menú\n")

#inicio
opc = 1
case = 1
Delete = 0
carrito = []
pagar = []
q = []
coin = 0
while opc != 5:
    menu()
    opc = variableMenu(opc)
    productos = ["Botella de agua 50 ml", "Pieza de pan", "Leche de 1lt", "Pack de 6 huevos","Mermelada de 400gr", "Mayonesa de 440gr","Galletas"]
    precios = [10, 6, 23, 25, 31, 23, 37]
    if opc == 1:
        producto(productos,precios)
        agregar(case)
    if opc == 2:
        verCarrito(q)
    if opc == 3:
        eliminarCarrito(Delete)
    if opc == 4:
        cajero(pagar)
        carrito = []
        pagar = []
        q = []

