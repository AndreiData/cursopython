
#Proyecto Fundamentos de Python M2 4M
#Por Yamil Andrei Espinoza Bernal

#Validación y operaciones de datos

#Crearemos un pequeño menu para poder interactuar con cada programa de manera individual, haciendo uso de un bucle "While True".
while True:
    print("\n--- Menú Principal ---")
    print("1. Encontrar el cuadrante de una coordenada")
    print("2. Validar la longitud de una palabra")
    print("3. Salir")

    # Pide al usuario que seleccione una opción del menú y se guarda en la variable "opcion_p":
    opcion_p = input("Selecciona una opción (1, 2, 3): ")

    # Si la variable de "opcion_p" es "1", ejecuta el programa para encontrar el cuadrante
    if opcion_p == "1":
        #Iniciamos un bucle "While True" para poder realizar la operación un número ilimitado de veces:
        while True:
            
            #Se solicita al usuario si desea agregar coordenadas o terminar:
            opcion = input("Agregar coordenadas (1) o terminar proceso (2): ")

            #Romper en bucle en caso de seleccionar la opción 2 (Terminar proceso):
            if opcion == "2":
                print("Proceso terminado. ¡Hasta luego!")
                break

            #Si la opción es 1, continuamos la lógica del cuadrante utilizando "elif":
            elif opcion == "1":
                try:
                    
                    #Solicitaremos las coordenadas al usuario, estas seran registradas en las variables "x" e "y" como número entero:
                    x = int(input("Ingresa el valor de X (Ingrese un valor diferente a 0): "))
                    y = int(input("Ingresa el valor de Y (Ingrese un valor diferente a 0): "))

                    #Se verifica que las coordenadas ingresadas no sean igual a 0:
                    if x == 0 or y == 0:
                        print("No se pueden identificar puntos en los ejes cuando alguna coordenada es 0. Intente nuevamente con valores diferentes a 0.")
                    
                    #Determinaremos el cuadrante basandose en los signo de X e Y:
                    else:
                        if x > 0 and y > 0:
                            print(f"Tu coordenada ({x},{y}), esta en el Cuadrante I.")
                        elif x < 0 and y > 0:
                            print(f"Tu coordenada ({x},{y}), esta en el Cuadrante II.")
                        elif x < 0 and y < 0:
                            print(f"Tu coordenada ({x},{y}), esta en el Cuadrante III.")
                        elif x > 0 and y < 0:
                            print(f"Tu coordenada ({x},{y}), esta en el Cuadrante IV.")
                
                #Si el usuario ingresa algo que no es un número para las coordenadas X o Y, el programa no se detendrá, sino que mostrará un mensaje de error y le permitirá intentarlo de nuevo.
                except ValueError:
                    print("Por favor ingrese un número valido.")

            #Si al momento de ingresar una opción que no sea agregar coordenadas (1) o terminar proceso (2) informará que la opción no es válida, y el bucle volverá a empezar.
            else:
                print("Opción no válida. Por favor, seleccione 1 para agregar coordenadas o 2 para terminar.")

    #Si la "opcion_p" es "2", ejecuta el programa para validar la longitud de una palabra.
    elif opcion_p == "2":
        
        #Crearemos la variable "palabra" que sera igual a un "input" del usuario. Pediremos se ingrese una palabra:
        palabra = input("Ingrese una palabra con longitud entre 4 y 8 caracteres: ")

        #Ahora obtendremos la longitud de la palabra con apoyo de la funcion "len" y la guardaremos en la variable "longitud".
        longitud = len(palabra)

        #Se verificara si la "longitud" de la palabra esta dentro del rango correcto (entre 4 y 8):
        #Utilizando la función "if" se realizara la verificación.
        if 4<= longitud <=8:
            print(f"La palabra {palabra} es correcta. Tiene {longitud} letras!")
        elif longitud < 4:
            print(f"La palabra {palabra} es demaciado corta. Solo tiene {longitud} letras.")
        else: #la longitud por descarte es mayor a 8 letras.
            print(f"La palabra {palabra} es demaciado larga. Tiene {longitud} letras.")
    
    # Si la "opcion_p" es "3", sale del bucle principal y termina el programa.
    elif opcion_p == "3":
        print("Proceso terminado. ¡Nos vemos!")
        break
    
    # Si la opción ingresada no es 1, 2 o 3, muestra un mensaje de error y vuelve a pedir nuevamente la opción.
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")