import sys
from lexico import AnalizadorLexico

def main():

    cadena = str(input("Dijite el codigo a evaluar: "))
   
    if len(cadena) <= 0:
        print(cadena + " No es un valor valido")
    else:
        analizador = AnalizadorLexico(cadena)

        print("\n\n")
        print("Resultado del analisis lexico:")
        print("\n")
        print('{:<30}'.format("Simbolo") + '{:<30}'.format("Tipo") + '{:<5}'.format("Codigo de Tipo"))

        while analizador.caracter != "$":
            analizador.siguienteSimbolo()
            print('{:<30}'.format(analizador.simbolo) + '{:<30}'.format(analizador.tipoCadena(analizador.tipo)) + '{:<5}'.format(str(analizador.tipo)))

if __name__ == '__main__':
    main()