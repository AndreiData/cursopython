a = float(input("Asigna primer numero:" ))
s = input("Asigna la operacion (+,-,*,/):" )
b = float(input("Asigna el segundo numero:" ))

if s == "*":10
    print(a * b)
elif s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "/": #INDIVISIBLE EN 0 AGREGAR OTRO IF
    print(a / b)
else:
    print("Error al elegir la operación")