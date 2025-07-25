print('''
Bienvenido a la calculadora de Indice de Masa Corporal (I.M.C)

    Instrucciones: 
    Por favor leé con atención los datos que se te solicitan 
    e ingresalos en el formato que se te indican para evitar errores. 
    Muchas gracias y suerte! 
           
''')

# *** *** LISTADO DE ERRORES COMUNES *** ***

e00 = str('Error:')
e01 = str('No puede dejar este campo vacío.')
e02 = str('Por favor, intentelo nuevamente.')
e03 = str('Se ingreso un dato invalido.')
e04 = str('Por favor, ingrese un valor numérico.')


# *** *** CAMPO DE NOMBRE *** ***

while True:
    n = input('Por favor, ingrese unicamente sus nombres: ').title()
    if not n.strip():
        print('{} {} {}'.format(e00, e01, e02))
    elif not n.replace(" ","").isalpha():
        print('{} {} {}'.format(e00, e03, e02))
    else:
        break


# *** *** CAMPO DE APELLIDO PATERNO *** ***


while True:
    p = input('Ingrese su apellido paterno: ').title()
    if not p.strip():
        print('{} {} {}'.format(e00, e01, e02))
    elif not p.isalpha():
        print('{} {} {}'.format(e00, e03, e02))
    else:
        break


# *** *** CAMPO DE APELLIDO MATERNO *** ***

while True:
    m = input('En caso de tener, ingrese su apellido materno, en el caso contrario dejar esta campo vacío: ').title()
    if m.strip() and not m.isalpha():
        print('{} {} {}'.format(e00, e03, e02))
    else:
        break


# *** *** CAMPO DE EDAD *** ***


while True:
    edad_str = input('Por favor, ingrese su edad: ')
    
    if not edad_str.strip():
        print('{} {} {}'.format(e00, e01, e02))
        continue

    try:
        edad = int(edad_str)
        if edad > 0:
            break
        else:
            print('{} {} La edad debe ser un número entero superior a 0. {}'.format(e00, e03, e02))
    except ValueError:
           print('{} {} {}'.format(e00, e03, e04))


# *** **** CAMPO DE PESO *** ***


while True:
    peso_str = input('Por favor, ingrese su peso en kilogramos (KG): ')
    
    if not peso_str.strip():
        print('{} {} {}.'.format(e00, e01, e02)) 
        continue

    try:
        kg = float(peso_str)
        if kg > 0:
            break
        else:
            print('{} {} El peso debe ser un número superior a 0. {}'.format(e00, e03, e02))
    except ValueError:
           print('{} {} {}'.format(e00, e03, e04))


# *** *** CAMPO DE ESTATURA *** ***


while True:
    estatura_str = input('Por favor, ingrese su estatura en metros: ')

    if not estatura_str.strip():
        print('{} {} {}.'.format(e00, e01, e02))
        continue

    try:
        es = float(estatura_str)
        if es > 0:
            break
        else:
            print('{} {} La estatura debe ser un número superior a 0. {}'.format(e00, e03, e02))
    except ValueError:
        print('{} {} {}'.format(e00, e03, e04))


# *** *** CALCULO MATEMATICO *** ***

imc = float("{:.2f}".format(float(kg / (es**2))))


# *** *** EVALUACIÓN DE IMC *** ***

c = ' '

if imc <= 18.49:
    c = 'peso bajo'
elif imc >= 18.50 and imc <= 24.99:
    c = 'peso normal'
elif imc >= 25.00 and imc <= 29.99:
    c = 'sobrepeso'
elif imc >= 30.00 and imc <= 34.99:
    c = 'obseidad leve'
elif imc >= 35.00 and imc <= 39.99:
    c = 'obesidad media'
elif imc >= 40.00:
    c = 'obesidad mórbida'


# *** *** IMPRIMIR LOS RESULTADOS *** ***

print(f'''

Resultados de la Evaluación

Nombre: {n} {p} {m}.
Edad: {edad} Años.
Peso: {kg} Kg.
Estatura: {es} m.

Tu I.M.C. es de {imc}, tienes {c}.

      ''')

input("Presiona Enter para salir...")

#Codigo realizado por Yamil Andrei Espinoza Bernal.
#Ucamp: Fundamentos de Python.
#Finalizado el día 24 de julio de 2025.