lista=[432, 331, 192, 108, 180, 50, 231, 188, 105, 51, 364, 168, 344, 195, 297, 342, 292, 198, 448, 62, 236, 342, 63] 
key="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

resultado=""

def modInverse(A,  M):
    X=1
    for X in range (1,M):
        if ((A*X)%M==1):
            print(X)
            return X

for i in lista:
    num = modInverse(i, 41)
    resultado+=key[num-1]


print(resultado)