# Proyecto final
![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/d8df42ebcd4697c858072bb09814f356de0f81ba/proyecto%20final/capturas/logo.png)

Centro Universitario De Ciencias Exactas e Ingenieria

Seminario de Solucion de problemas de Traductores 2

Profesor: Dr Michel Emanuel Lopez Franco

Sección: D02

Alumno: Jesus Fernando Garcia Santos

Codigo: 213623791

## Introduccion
El objetivo de esta practica es generar un compilador que use un analizador sintactico,lexico y semantico y que sea feable utilizaremos los tokens mas comunes y una tabla de compiladores que se nos a dado en formato lr.
Mostraremos un vistaso de cada parte del compilador pero para su mayor estudio se dejara tanto el codigo en el repositorio asi como los documentos que utilize para la practica.

### Analizador lexico
Se define nustros tokens para la creacion de nuestro analizador lexico como se explica en la imagen ,en mi caso le di un numero unico a cada expresion listados en una lista y asi ponerle a cada uno su metodo  y defini cada uno con una funcion.
![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/7db8d6f06ffd31a8c169a86b8f4776362c31e79f/proyecto%20final/capturas/lexico.png)
### Analizador Sintactico
Definimos las reglas sintacticas y leemos el documento proporcionado por el profesor llamado compilador .lr que es la tabla estados, que nos proporciona la informacion de que tipo de variables o tipo de accion estamos ejecutando y asi sacar un lenguaje mas completo que nos sevira de apollo para el anamizador semantico.

compilador.lr 
[click aqui](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/08d05d43104c78dda0fb54accf9e12fa98227724/proyecto%20final/compilador.lr)

![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/7db8d6f06ffd31a8c169a86b8f4776362c31e79f/proyecto%20final/capturas/sintactico.png)

### Analizador semantico
Como se dijo anteriormente con el analizador sintactico este nos ayuda a vereficar si la informacion dada es correcta y en el caso de que sea fiable se realiza la traducccion del texto que en en este proyecto lo utilizaremos como un txt puede ser de cualquier compilador pero antes tiene que darse  la direccion  y termino del texto a traducir, al terminar de traduccir nos arrojara una lista de datos que nos ayuda a conocer la naturaleza del texto y sobre todo a la creacion del arbol.

![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/08d05d43104c78dda0fb54accf9e12fa98227724/proyecto%20final/capturas/semantico.png)
En ese apartado tambien se creo una  funcion para detectar los datos y asi crear el arbol.

![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/7db8d6f06ffd31a8c169a86b8f4776362c31e79f/proyecto%20final/capturas/arbol.png)

### Proyecto
Para la compilacion y decodificacion del programa utilize python 3.9 (es necesario tenerlo actualizado en el caso de compilar) y tkinter para seleccionar el archivo que decea traducir, ya que esta nos brinda de una herramienta  para ser mas practica la visualizacion de nuestros ficheros en mi caso lo dirigi el directo a la carpeta de pruebas y que busque los archivos con la extencion .txt
![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/7db8d6f06ffd31a8c169a86b8f4776362c31e79f/proyecto%20final/capturas/1.png)

Al darle a compilar el programa inica normalmente y nos pide el directorio del archivo a traducir, lo selecciona y comienza a traducir en este caso utilizaremos p1 que es el que se muestra  a continuacion, tambien el p2 los dos con la extencion txt.

![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/08d05d43104c78dda0fb54accf9e12fa98227724/proyecto%20final/capturas/suma.png)

![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/08d05d43104c78dda0fb54accf9e12fa98227724/proyecto%20final/capturas/sumafloat.png)

este es le resultado del compilador ,pero al parecer yo tengo un problema de logica ya que al terminar de compilar el programa truena de manera inesperada pero solo al final de compilar. Algunos de los inconvenientes que tiene el programa es que no lee algunos signos como <> ya que me daba problemas  y esa fue la unica solucion rapida que enconte que era desabilitar esa opcion 
![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/7db8d6f06ffd31a8c169a86b8f4776362c31e79f/proyecto%20final/capturas/2.png)
![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/7db8d6f06ffd31a8c169a86b8f4776362c31e79f/proyecto%20final/capturas/3.png)
este es el arbol utilizando drawio
![](https://github.com/Jesus-garcia122/seminario-de-traductores/blob/08d05d43104c78dda0fb54accf9e12fa98227724/proyecto%20final/capturas/ejemplo1.png)
### Conclusiones 
en conclusion este entregable se me complico demaciado en primer lugar por que nunca habia usado pithon lo havia usado pero por muy ensima y dar el brinco a crear un analizador fue mucho por eso es el motivo que tarde tanto en entender el duncionamiento ,por otro lado fue de mucha ayuda ya que tengo mas nocion de como es que un compilador funciona pero al final de todo logre terminarlo no le la mejor forma que me ubiera gusto terminarlo pero me diverti y aprendi muchas cosas y eso para mi es mas que suficiente espero y volver a tener mas retos como este que me ayuden a crecer .

### Referencias
https://app.diagrams.net/#
