# Proyecto Fundamentos de Python M2  

## 📌 Descripción  
Este proyecto consiste en un programa interactivo en Python que utiliza un **menú principal** para acceder a dos funcionalidades:  

1. **Identificación de cuadrantes**: Permite ingresar coordenadas (x, y) y determina en qué cuadrante del plano cartesiano se encuentra el punto.  
2. **Validación de palabras**: Verifica si la longitud de una palabra ingresada por el usuario está dentro del rango de **4 a 8 caracteres**.  

El programa se ejecuta en un bucle hasta que el usuario decida salir.  

---

## 🏗️ Diseño del programa  
El programa fue diseñado de forma modular y simple, con las siguientes características:  

- Uso de un **menú principal** para seleccionar las opciones.  
- Estructuras de control como `while True`, `if-elif-else` para la navegación y validaciones.  
- Manejo de errores con `try-except` para evitar que el programa se detenga cuando se ingresa un valor inválido.  
- Validaciones lógicas que permiten que el usuario interactúe de manera continua hasta decidir salir.  

---

## 📂 Estructura del archivo  
El código se encuentra en un único archivo:  

```
YAMIL_ESPINOZA_proyectoM2.py
```

Estructura del flujo principal:  

```
while True:
    Mostrar menú principal
    Opción 1 → Ejecuta lógica de cuadrantes
    Opción 2 → Ejecuta validación de palabra
    Opción 3 → Termina programa
    Otro → Muestra error y repite menú
```

---

## ⚙️ Funcionamiento  

### 1. Menú Principal  
- El usuario elige entre 3 opciones:  
  - (1) Encontrar cuadrante.  
  - (2) Validar longitud de palabra.  
  - (3) Salir del programa.  

### 2. Encontrar el cuadrante de una coordenada  
- El usuario ingresa valores enteros para **X** y **Y**.  
- Se determina en qué cuadrante se encuentra el punto:  
  - **Cuadrante I:** X > 0, Y > 0  
  - **Cuadrante II:** X < 0, Y > 0  
  - **Cuadrante III:** X < 0, Y < 0  
  - **Cuadrante IV:** X > 0, Y < 0  
- Si alguna coordenada es igual a 0, se notifica que no es posible identificar cuadrante.  
- Incluye manejo de errores en caso de ingresar datos no numéricos.  

### 3. Validación de longitud de una palabra  
- El usuario ingresa una palabra.  
- Se valida su longitud:  
  - Correcta: entre 4 y 8 caracteres.  
  - Demasiado corta: menos de 4 caracteres.  
  - Demasiado larga: más de 8 caracteres.  

### 4. Salida del programa  
- El usuario puede seleccionar la opción (3) en el menú principal para terminar la ejecución.  

---

## ▶️ Ejecución  

1. Clonar o descargar este repositorio.  
2. Ejecutar el programa con Python 3:  

```bash
python YAMIL_ESPINOZA_proyectoM2.py
```

3. Seguir las instrucciones del menú.  


---

## 👨‍💻 Autor  
**Yamil Andrei Espinoza Bernal**  
Proyecto para **Fundamentos de Python M2 - 4M**  
