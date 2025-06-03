dicc = {}
ok = False
cont = 0
cont2 = 0
ok2 = False
while ok == False:
 try:
    cant_pa = int(input("Ingrese la cantidad de pacientes a registrar: "))
    for i in range(cant_pa):
        
        while ok2 == False:
            nombre = input(f"Ingrese el nombre del paciente {i + 1}/{cant_pa}: ")
            dicc["nombre"] = nombre
            try:
                edad = int(input("Ingrese la edad del paciente: "))
                if edad < 0:
                    print("Ingrese un número válido, mayor o igual a 0")
                elif edad <= 60:
                    dicc["edad"] = edad
                    cont += 1
                    print("60 años o menos")
                else:
                    cont2 += 1
                    dicc["edad"] = edad
                    print("Mayor de 60 años")
                ok2 = True
            except ValueError:
                print("Debe ingresar un número entero.")
    ok = True 
    print(f"Se registraron {cont} pacientes de 60 años o menos.")
    print(f"Se registraron {cont2} pacientes Mayores de 60 años.")
    
 except ValueError:
    print("Debe ingresar un número entero.")