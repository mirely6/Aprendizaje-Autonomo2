#Ejercicio del diagrama de flujo
print("Lista de productos disponibles")
producto= input("Ingrese el producto que desee:")
if producto == "Laptop":
    cantidad = input("Ingrese la cantidad:")
    pago = int(input("Ingrese el pago:"))
    while pago < 500:
        print("Pago insuficiente, por favor ingrese el valor completo")
        pago = int(input("Ingrese nuevamente el pago:"))
    print("Factura generada correctamente")
else:
    print("Producto no disponible")