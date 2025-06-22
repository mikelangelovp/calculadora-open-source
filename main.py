import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    while True:
        print("\nCalculadora Open Source")
        print("1. Sumar 2 números")
        print("2. Restar 2 números")
        print("3. Multiplicar 2 números")
        print("4. Dividir 2 números")
        print("5. Suma avanzada (N números)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", sumar.sumar(a, b))

        elif opcion == '2':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", resta.restar(a, b))

        elif opcion == '3':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", multiplicacion.multiplicar(a, b))

        elif opcion == '4':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", dividir.dividir(a, b))

        elif opcion == '5':
            numeros = input("Ingresa los números separados por coma: ")
            lista = [float(x) for x in numeros.split(",")]
            print("Resultado:", suma_avanzada.suma_avanzada(lista))

        elif opcion == '6':
            print("Gracias por usar la calculadora.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()
