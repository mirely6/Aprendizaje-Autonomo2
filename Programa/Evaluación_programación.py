#Lista de productos
productos = ["Laptop", "Mouse", "Teclado"]
#Tupla con precios
precios = (500, 20, 30)
#Diccionario producto precio
catalogo = {
    "Laptop": 500,
    "Mouse": 20,
    "Teclado": 30
}
#Función para procesar la compra
def comprar_producto():
    print("Lista de productos disponibles:")
    print(productos)

    producto = input("Ingrese el producto que desee: ")

    if producto in catalogo:
        cantidad= int(input("Ingrese la cantidad:"))

        total= catalogo[producto]*cantidad
        print("Total a pagar: $", total)

        pago= int(input("Ingrese el pago: "))

        while pago < total:
            print("Pago insuficiente, por favor ingrese el valor completo")
            pago = int(input("Ingrese nuevamente el pago: "))

        cambio = pago - total

        print("Factura generada correctamente")
        print("Producto: ", producto)
        print("Cantidad: ", cantidad)
        print("Cambio: $", cambio)

    else:
        print("Producto no disponible")

#Llamada a la función
comprar_producto()