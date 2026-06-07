def Factorial(numero):
    cont=1
    if(numero==0): return cont
    else:
        for i in range(1,numero+1,1):
            cont*=i
        return cont


def GenerarCodigo(palabra):
    longitudPalabra=len(palabra)
    codigo=""
    for i in range(0,longitudPalabra,1):
        if(i==0):
            codigo+=palabra[i]
        if(i==2):
            codigo+=palabra[i]
    codigo+=palabra[longitudPalabra-1]
    codigo+=str(longitudPalabra)
    return codigo


def NumParImpar(numero):
    if(numero%2==0):
        return 0
    else: return 1
def calcularFD(resultadoDiv,numero):
    fd=1
    for i in range(numero,0,-1):
            print("Indice: ",i)
            if(i>0):
                if(i%2==resultadoDiv):
                    print("Numero que ingresa: ",i)
                    fd*=i
                    print("Contador Acumulado: ",fd)
            else:
                break
    return fd

def FactorialDoble(numero):
   rd=NumParImpar(numero)
   fd=calcularFD(rd,numero)
   return fd



def OperacionFactorial(opcion,numero):
    resultado=0
    if(opcion=="Factorial"):
        resultado=Factorial(numero)
    elif(opcion=="Factorial Doble"):
        resultado=FactorialDoble(numero)
    return resultado
