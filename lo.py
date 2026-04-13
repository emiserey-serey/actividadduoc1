try:
    edad = int(input("ingrese su edad:"))
    if edad >18:
        print("es mayor de edad")
    else:
        print("es menor de edad")
except:
    print("el valor ingresado debe ser numérico")


user1 = "emi"
contraseña1 = "lolita12"
user2 = "juan"
contraseña2 = "lolita12"
user = input("ingrese su usuario:")
contraseña = input("ingrese su contraseña:")
if user == user1 and contraseña == contraseña1 or user == user2 and contraseña == contraseña2 :
    print("Bienvenido")
else:
    print("credenciales incorrectas")
    





































