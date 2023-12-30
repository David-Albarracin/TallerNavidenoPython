
![Logo](https://www.python.org/static/img/python-logo.png)



# Taller Practico Navideño 

Este taller está diseñado con pautas específicas que facilitarán la comprensión del código contenido en los archivos.



## Pautas Generales


1. **Estructura de Carpetas:**
    El proyecto está organizado en carpetas con nombres relacionados a taller y los 100 ejercicios.

      - **(100_Ejercicios_py):**
         Contiene 100 ejercicios en Python, numerados del 1 al 100.py. Incluye un archivo [reusable.py](https://github.com/David-Albarracin/TallerNavidenoPython/blob/main/100_Ejercicios_py/reusable.py) que alberga funciones reutilizadas en varios ejercicios. Cada ejercicio (n.py) incluirá un comentario explicativo del problema a solucionar.

      - **(Nivel_Principiante):**
        Contiene los 3 ejercicios del taller de navidad de nivel principiante. El análisis de cada ejercicio proporcionará una explicación concisa de cómo se resolvió.

      - **(Nivel_Intermedio):**
         Incluye los 3 ejercicios del taller de navidad de nivel intermedio. Cada ejercicio, detallado en la sección de análisis, presenta una explicación de su solución.

      - **(Nivel_Experto):**
         Contiene el único ejercicio del taller de navidad de nivel experto, organizado en módulos. Para probar este ejercicio, se debe ejecutar el archivo main.py.

      - **(Nivel_Avanzado):**
         Similar a la carpeta de Nivel Experto, contiene el único ejercicio de nivel avanzado dividido en módulos. La ejecución exitosa implica ejecutar el archivo main.py.

3. **Variables Comentadas:**
    Cada variable contiene un comentario descriptivo justo encima de ella para proporcionar información sobre el tipo de datos que almacena no aplicable a (100_Ejercicios).

4. **Funciones Documentadas:**
    Las funciones incluyen comentarios que explican el proceso que llevan a cabo. Estos comentarios proporcionan detalles sobre la funcionalidad de la función y el valor que se espera que retorne.

## Contribuciones

Estas prácticas estructuradas y documentadas facilitarán la comprensión y colaboración en el desarrollo de software, siguiendo las mejores prácticas de la comunidad de desarrollo; Si desea Mas Informacion relacionados con los 100 ejercicios lo invito a visitar [100 EJERCICIOS PSEING](https://www.youtube.com/watch?v=3CNVzw4Kee0&list=PLtzBCV-VcS_TsqlBrmWoq_f0MR7WIpJS9&index=1).

# Análisis:

## Nivel Principiante:

-  **Ejercicio 1**

   - **Descripción del Problema:**
      Se requiere realizar un programa en Python que permita leer 3 números enteros positivos e imprima la sumatoria de los tres números.

   - **Solución Propuesta:**
      Para abordar esta problemática, comenzamos declarando tres variables destinadas a almacenar el número ingresado, la lista de números y la suma de estos. Con el fin de gestionar posibles errores y asegurar la entrada de números positivos únicamente, incorporaremos un bucle while que permanecerá en ejecución hasta que tengamos los tres números requeridos. Estos números se almacenarán en la variable "numeros", la cual se convertirá explícitamente a tipo entero. A continuación, se verificará si el número es positivo y se guardará en la lista "listNumbers". Posteriormente, se sumará a la variable "suma" una vez confirmada su positividad.
      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |numero|Entrada|int()|
      |listNumbers|Salida|list()|
      |suma|Salida|int()|


-  **Ejercicio 2**

   - **Descripción del Problema:**
      El Centro de Salud de Campuslands busca desarrollar un programa para calcular el Índice de Masa Corporal (IMC) de 20 estudiantes nuevos. El programa deberá mostrar el nombre del estudiante, la edad, el IMC y la categoría correspondiente. Además, se requiere generar un informe con pautas indicadas

   - **Solución Propuesta:**
      Para abordar esta problemática, comenzamos generando un ciclo que requiera el registro de 20 estudiantes luego le pediremos al usuario que ingrese los datos segun la estructura del estudiante que nos ayudara a almacenar los datos
      ```python
      estudiante = {
         "nombre": nombre,
         "edad": f"{edad} Años",
         "peso": f"{peso} Kg",
         "altura": f"{altura} Mts",
         "imc": imc,
         "rango": imcRango
      }
      ```
      Luego de Pedirle los datos necesarios generaremos el valor de imc = peso / (altura * altura) y llamaremos a la funcion getRango_IMC(imc) esta nos retorna el rango en el que se encuentra el estudiante dependiendo de su imc como Peso Ideal, Sobre peso .....

      Teniendo Estos Datos Generamos en pantalla un informe con los datos requeridos
      

   - **Tabla de Declaración de Variables:**
      | Nombres   | Tipo E/S  |  Tipo     |
      |-----------|-----------|-----------|
      |reporte|Salida|dict()|
      |estudiantes|Salida|list()|
      |estudiante|Salida|dict()|
      |imc|Salida|float()|