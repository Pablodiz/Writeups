lista=[128 ,322 ,353, 235, 336 ,73 ,198, 332, 202, 285, 57 ,87 ,262, 221 ,218 ,405 ,335, 101 ,256, 227 ,112 ,140] 

key="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

resultado=""

for i in lista:
    num = i%37
    resultado+=key[num]


print(resultado)