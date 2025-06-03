ok = False
total_e = 0


print("******CINE ESTRELLA******\nBienvenido al sistema de venta de entradas del Cine Estrella.")
print("**"*5)

while ok == False:
     try:
        op = int(input("1.Ver entradas disponibles\n2.Comprar entradas\n3.Cargar entradas\n4.Salir\n*********"))
    
        if op == 1:
            print(f"Las entradas disponibles: {total_e}")
            print("**"*5)

        elif op == 2:
            entradas = int(input("Cuántas entradas desea comprar?: "))
            
            if entradas < total_e:
                total_e = total_e - entradas
                print(f"Compra exitosa. Quedan {total_e} entradas")
                print("**"*5)
            
            elif entradas > total_e:
                print(f"No hay suficientes entradas. Total disponible: {total_e}")
                print("**"*5)
        elif op == 3:
            cargar = int(input("Cuántas entradas desea cargar?: "))

            if cargar <= 0:
                print("Ingrese un número válido.")
                print("**"*5)
            else:
                total_e = cargar + total_e
                print(f"Se han cargado {cargar}. Total disponible: {total_e}")
                print("**"*5)
        elif op == 4:
            print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
            print("**"*5)
        else:
            print("Opción inválida.")
            print("**"*5)
     except ValueError:
        print("Ingrese números enteros.")