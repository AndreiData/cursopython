# **Título:** Calculadora de Índece de Masa Corporal (IMC)

    Por Yamil Andrei Espinoza Bernal 

    UCAMP: M1 4M Proyecto Fundamentos de Python
    Tijuana, Baja California para jueves 24 de julio de 2025

---

### **Descripción:**
Este programa es una calculadora interactiva de Índice de Masa Corporal, por sus siglas IMC; desarrollada en Python.
Permite al usuario ingresadno sus datos personales como nombre, apellido, edad, peso y altura. 
Luego, calcula el IMC y clasifica el resultado según el estandar de rangos ofrecidos por el ISSSTE (peso bajo, normal, subrepeso, obesidad leve, moderada o mórbida).
El programa incluye validaciones para asegurar que la entrada de datos del usuario sea correcta, mostrando mensajes de error específicos (datos vacíos, inválidos o no numéricos).

---

### ¿Cómo funciona el programa?

1. **Bienvenida e instrucciones**: Al iniciar, el programa saluda al usuario y proporciona instrucciones sobre el formato de entrada de datos para evitar errores.
2. **Recolección de Datos del Usuario**:
    * Se solicita el nombre(s) del usuario.
    * Se pide el apellido paterno.
    * Se permite ingresar un apellido materno (opcional).
    * Se solicita la edad.
    * Se solicita el peso en Kilogramos (KG).
    * Se solicita la estatura en metros (m).
    * Cada campo de entrada incluye un bucle *while True* para asegurar que el usuario ingrese datos válidos antes de continuar.
3. **Validación de Entrada:**
    * El programa verifica que ningún campo obligatorio se deje vacío.
    * Se valida que los campos de nombre y apellidos contengan solo caracteres alfabéticos.
    * Para la edad, peso y estatura, se utiliza *try-except ValueError* para asegurar que los datos ingresados sean numéricos.
    * Además, se verifica que la edad, el peso y la estatura sean valores positivos.
    * En caso de error, se muestra un mensaje descriptivo y se solicita al usuario que intente de nuevo.
4. **Cálculo de IMC:**
    * Una vez que se tienen todos los datos válidos, se calcula el IMC utilizando la formula  *IMC=peso(kg)/altura(m)^2*.
    * El resultado se formatea a dos decimales.
5. **Evaluación y Clasificación de IMC:**
    * El IMC calculado se compara con rangos predefinidos para clasificar el estado de salud.
    * Estos rangos fueron tomados de la pagina oficial de [ISSSTE](https://www.gob.mx/issste/es/articulos/que-es-el-indice-de-masa-corporal?idiom=es):
        * Menor o igual a 18.49: Peso bajo.
        * Entre 18.50 y 24.99: Peso normal.
        * Entre 25.00 y 29.99: Sobrepeso.
        * Entre 30.00 y 34.99: Obesidad leve.
        * Entre 35.00 y 39.99: Obesidad media
        * Mayor o igual a 40.00: Obesidad mórbida.
6. **Resultados:** Finalmente, el programa imprime un resumen completo que incluye el nombre del usuario, edad, peso, altura, el valor de su IMC y la clasificación de su estado corporal.

---

### Proceso técnico y desarrollo.

El desarrollo se dio de manera modular y estructurada, para facilitar su lectura, y su mantenimiento y modificación.

1.  **Manejo de Entrada del Usuario (Loops de Validación):**
    * Cada solicitud de datos (nombre, apellidos, edad, peso, estatura) se encapsuló dentro de un bucle `while True`. Esto para que el programa no avance hasta que el usuario proporcione una entrada válida para cada campo.
    * Se utilizaron métodos de cadena como `.strip()` para verificar campos vacíos y `.isalpha()` para asegurar que los nombres contengan solo caracteres alfabéticos.
    * Para datos numéricos (edad, peso, estatura), se implementaron bloques `try-except ValueError`. Esto captura específicamente los errores cuando la entrada no puede ser convertida a un número entero o flotante, indicando al usuario que ingrese un valor numérico.
    * Adicionalmente, se incluyeron validaciones lógicas para asegurar que los valores numéricos (edad, peso, estatura) fueran positivos y mayores a 0.

2.  **Definición de Errores Comunes:** Se establecio un estandar de mensajes de error (`e00` a `e04`) que permite reutilizar los mensajes y evitar una saturación de texto y mensajes para errores comunes, y facilita  la lectura del código.

3.  **Cálculo Central del IMC:** La lógica principal y finalidad del programa se centró en la fórmula del IMC, `peso / (estatura**2)`. Se utilizó `float("{:.2f}".format(...))` para redondear el resultado a dos decimales y asi evitar la complejidad de manejar demasiados decimales.

4.  **Clasificación Condicional del IMC:** Se utilizó una serie de sentencias `if-elif-else` para clasificar el IMC calculado en diferentes categorías (peso bajo, normal, sobrepeso, obesidad, etc.). Esta estructura condicional es eficiente para manejar los múltiples rangos y asignar una descripción textual a la variable `c` que interpreta el resultado numérico.

5.  **Presentación de Resultados:** Finalmente, se utilizo una f-string(`f'''...'''`) para una salida clara y formateada facilitando la inserción de variables en la cadena del mensaje que resume todos los datos ingresados por el usuario y el resultado de la evaluación del IMC. 

6. **Presiona Enter para salir...** Una vez que los resultdos son impresos, el programa ejecutado se cierra por si mismo, no dando tiempo a ver los resultados. Esto se soluciono, integrando al final del codigo un `input(Presiona Enter para salir...)`, de esta manera el programa se quedaria estatico hasta que el usuario optara por presionar la tecla `Enter`.
---

### Reflexión sobre el Bootcamp:

La aplicación de variables, operadores y cadenas de texto resultaron un elemento fundamental en el diseño y la estructuración de todo el código. Pudiendo desarrollar una versión sencilla del programa con elementos básicos y sencillos, que sería el punto de partida.

Sin embargo, algo importante y tal vez un poco más que estos fundamentos, es la lógica, la creatividad, el pensamiento analítico y crítico. Estos elementos son cruciales para abordar problemas de manera efectiva, diseñar soluciones eficientes y pensar más allá de la sintaxis básica del lenguaje.

Esta reflexión la puedo dictaminar de cierta, porque desde mis sentidos, hablando como persona, es dificil programar, es aun mas dificil llegar al resultado que quieres. Pero debo decir, que es satisfactorio, el haber conseguido que el programa funciones.

---
---