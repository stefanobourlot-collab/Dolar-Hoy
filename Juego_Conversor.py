# Definimos la "máquina" de saludar
def saludar_usuario(nombre):
    print(f"¡Hola Stefano Bourlot! Bienvenido a tu sistema.")

# La usamos (la llamamos)
saludar_usuario("Stefano Bourlot")

def conversor():
    try:
        pesos = float(input("Pesos a convertir: "))
        print(f"Son ${round(pesos/950, 2)} USD")
    except ValueError:
        print("❌ Error: Por favor, ingresa solo números, no letras.")
def juego():
    print("Jugando a adivinar...")
    import random

    
    secreto = random.randint(1, 100)
    tus_numeros = []
    
    while True:
        try:
            intento = int(input("Introduce un número: "))
        except ValueError:
                print("❌ Eso no es un número.")
                continue
        
        tus_numeros.append(intento)
        
        if intento == secreto:
            print("¡GANASTE!")
            print(f"Tus intentos fueron: {tus_numeros}")
            print(f"En total arriesgaste {len(tus_numeros)} veces.")
            break
        elif intento < secreto:
            print("Es más grande...")
        else:
            print("Es más chico...")# (Aquí podrías pegar el código del juego que ya hiciste)

while True:
    print("\n--- MI MULTI-APP ---")
    print("1. Conversor")
    print("2. Juego")
    print("3. Salir")
    
    opcion = input("Elegí una opción: ")
    
    if opcion == "1":
        conversor()
    elif opcion == "2":
        juego()
    elif opcion == "3":
        print("Cerrando sistema...")
        break
    else:
        print("Opción no válida")
