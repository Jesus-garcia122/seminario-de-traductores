# Proyecto final

Centro Universitario De Ciencias Exactas e Ingenieria

Seminario de Solucion de problemas de Traductores 2
Profesor: Dr Michel Emanuel Lopez Franco
Sección: D02
Alumno: Jesus Fernando Garcia Santos
Codigo: 213623791

## introduccion
El objetivo de esta practica es generar un compilador que use un analizador sintactico,lexico y semantico y que sea feable utilizaremos los tokens mas comunes y una tabla de compiladores que se nos a dadop en formato lr.

Mostraremos un vistaso de cada parte del compilador pero para su mayor estudio se dejara tanto el codigo en el repositorio asi como los documentos que utilize para la practica.

### Analizador lexico
Se define nustros tokens para la creacion de nuestro analizador lexico como se explica en la imagen ,en mi caso le di un numero unico a cada expresion listados en una lista y asi ponerle a cada uno su metodo  y defini cada uno con una funcion
### Analizador Sintactico
Definimos las reglas sintacticas y leeemos el documento proporcionado por el profesor llamado compilador .lr que es la tabla estados, que nos proporciona la informacion de que tipo de variables o tipo de accion estamos ejecutando y asi sacar un lenguaje mas completo que nos sevira de apollo para el anamizador semantico.
### Analizador semantico
Como se dijo anteriormente con el analizador sintactico este nos ayuda a vereficar si la informacion dada es correcta y en el caso de que sea fiable se realiza la traducccion del texto que en en este proyecto lo utilizaremos como un txt puede ser de cualquier compilador pero antes tiene que darse  la direccion  y termino del texto a traducir, al terminar de traduccir nos arrojara una lista de datos que nos ayuda a conocer la naturleza del texto y  sobre todo a la creacion del arbol .
### Proyecto
Para la compilacion y decodificacion del programa utilize python 3.9 (es necesario tenerlo actualizado en el caso de compilar) y tkinter para seleccionar el archivo que decea traducir, ya que esta nos brinda de una herramienta  para ser mas pratica la visualizacion de nuestros ficheros en mi caso lo derigi directo ala carpeta de pruebas y que busque los archivos con .txt

Al darle a compilar el programa inica normalmente y nos pide el directorio del archivo a traducir lo selecciona y comienza a traducir en este caso utilizaremos p1que es el que se muestra  a continuacion

este es le resultado del compilador ,pero al parecer yo tengo un problema de logica ya que al terminar de compilar el programa truena de manera inesperada pero solo al final de compilar. Algunos de los incobenientes que tiene el programa es que no leee algunos signos como <> ya que me daba problemas  y esa fue la unica solucion rapida que enconte que era desabilitar esa opcion 

### Conclusiones 
en conclusion este entregable se me complico demaciado en primer lugar por que nunca habia usado pithon lo avia usado pero por muy ensima y dar el brinco a crear un analizador fue mucho por eso es el motivo que tarde tanto en entender el duncionamiento ,por otro lado fue de mucha ayuda ya que tengo mas nocion de como es que un compilador funiona pero al final de todo logre terminarlo no le la mejor forma que me ubiera gusto termianrlo pero me diverti y aprendi muchas cosas y eso para mi es mas que suficiente espero y volver a tener mas retos como este que me ayuden a crecer .

### referencias
https://app.diagrams.net/#
