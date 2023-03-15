nombre = input("Ingresá el colegio: ")
viajeros = int(input("Ingresá la cantidad de egresados: "))
acompañantes = (viajeros // 30) + 1
precio = 50000*(viajeros + acompañantes)
print(f"El viaje sale ${precio}")