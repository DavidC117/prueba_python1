a=int (input ("escribe un numero positivo"))
while a < 0:
    print ("Ha escrito un numero negativo, intente de nuevo")
    a = int (input ("escriba un numero positivo"))
print ("gracias por su colaboracion")
input ("...")

#funcion

def suma (x,y):
    resul=x+y
    
    return resul

x=int (input ("digite su primer numero"))
y=int (input ("digite su segundo numero"))
resultado=suma (x,y)
print ("la suma de ",x,"+",y,"es:",resultado)

