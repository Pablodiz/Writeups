import math

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))  

def imprimir_resultado(matriz, railes: int, mensaje_cifrado: str):
    descendente = True
    fila = 0
    columna = 0
    resultado = ""
    for i in mensaje_cifrado:
        if fila == 0: 
            descendente = True 
        elif fila == railes - 1:
            descendente = False 
        
        resultado+=(matriz[fila][columna])

        if descendente: 
            fila = fila + 1 
        else: 
            fila = fila - 1 
        
        columna+=1

    return resultado

def denominador(N, x):
    return (N + ((N-1) * x))

# N + ((N-1) * x) = L + y
def resolver_ecuacion(N:int, L:int): 
    x = 1 
    while L > denominador(N, x):
        x=x+1
    y = denominador(N, x) - L 
    return x,y

def crear_grupos(K, filas_intermedias, N, mensaje_cifrado):
    grupos = []
    grupos.append(mensaje_cifrado[:K])
    for i in range (1, N-1):
        inicio = K + filas_intermedias*(i-1)
        fin = inicio + filas_intermedias 
        grupos.append(mensaje_cifrado[inicio:fin]) 
    grupos.append(mensaje_cifrado[-K:])
    return grupos

def crear_matriz(grupos, mensaje_cifrado, N):
    # Creo una matriz de huecos 
    matriz = [['.' for _ in range(len(mensaje_cifrado))] for _ in range(N)]

    descendente = True
    fila = 0
    columna = 0
    indices = [0 for _ in range(N)]
    for i in mensaje_cifrado:
        if fila == 0: 
            descendente = True 
        elif fila == N - 1:
            descendente = False 
        try:
            matriz[fila][columna] = grupos[fila][indices[fila]]
        except: # No hay más caracteres en el grupo
            pass 

        indices[fila]+=1
        if descendente: 
            fila = fila + 1 
        else: 
            fila = fila - 1 
        
        columna+=1

    return matriz

def rail_fence(railes: int, mensaje_cifrado: str) -> str:
    # Variables
    N = railes 
    L = len(mensaje_cifrado) 
    Periodo = 2 * (N - 1)
    K = L/Periodo
    if K%1!=0:         
        K = math.ceil(K)
        (x, y) = resolver_ecuacion(N, L)    
        diagonales = x+1
        # Diagonales pares, huecos rellenados desde segunda fila hacia atrás
        if diagonales%2==0:
            pass
        # Diagonales impares, huecos rellenados desde la última fila hacia atrás
        else:
            longitudes_intermedias_deberian_ser = 2 * K - 1  
            longitudes_intermedias_son = longitudes_intermedias_deberian_ser - 1 
            nuevo_mensaje_cifrado  = mensaje_cifrado[:-((y-1) * longitudes_intermedias_son + (K-1))]
            final = mensaje_cifrado[-(K-1):]
            partes = [final+"X"]
            for i in range(1,y):
                indice = len(mensaje_cifrado) - (K-1) -(longitudes_intermedias_son)*i 
                partes.append(mensaje_cifrado[indice:indice+longitudes_intermedias_son]+"X")


            for i in reversed(partes):
                nuevo_mensaje_cifrado+=i
                
            grupos = crear_grupos(K, longitudes_intermedias_deberian_ser, N, nuevo_mensaje_cifrado)

    else: 
        K = int(K)
        grupos = crear_grupos(K, 2*K, N, mensaje_cifrado=mensaje_cifrado)

    matriz=crear_matriz(grupos, mensaje_cifrado=mensaje_cifrado, N=N)
    imprimir_matriz(matriz)
    return imprimir_resultado(matriz=matriz, railes=railes, mensaje_cifrado=mensaje_cifrado)

print(rail_fence(3, "WECRUOERDSOEERNTNEAIVDAC"))
print(rail_fence(5, "HLERDLOLWO"))
print(rail_fence(4, "Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA"))



