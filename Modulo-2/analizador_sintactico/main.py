import sys
from sintactico import AnalizadorSintactico

def main():

    
    cadena = str(input("Escribe una cadena: "))

    print("\n\nResultado del analisis sintáctico:")
    if len(cadena) <= 0:
        print(cadena + " No es una cadena valida")
    else:
        analizador = AnalizadorSintactico()
        resultado = analizador.analizadorSintactico(cadena)
        
        if resultado:
            print("\n\nLa cadena es valida\n\n")
        else:
            print("\n\nLa cadena es invalida\n\n")
    # Fin del if-else

if __name__ == '__main__':
    main()