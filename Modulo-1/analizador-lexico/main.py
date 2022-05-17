import sys
from lexico import Analizador_Lexico

def main():
    cadena = str(input("digite la cadena que decea verificar: "))
    
    if len(cadena) <= 0:
        print(cadena + " No es una cadena valida")
    else: 
        analizador = Analizador_Lexico(cadena)
        print("\n**************************************************************")
        print("\t\tResultado del analisis lexico:")
        print("\n**************************************************************")
        print('{:<30}'.format("Simbolo") + '{:<30}'.format("Tipo") + '{:<5}'.format("Codigo de Tipo"))

        while analizador.caracter != "$":
            analizador.siguienteSimbolo()
            print('{:<30}'.format(analizador.simbolo) + '{:<30}'.format(analizador.tipoCadena(analizador.tipo)) + '{:<5}'.format(str(analizador.tipo)))
if __name__ == '__main__':
    main()