# ROT13
Instalo bsdgames en kali
echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}" | rot13

# Netcat
nc jupiter.challenges.picoctf.org 64287

# Convertir ASCII a texto


# Ltdis
```bash
#!/bin/bash



echo "Attempting disassembly of $1 ..."


#This usage of "objdump" disassembles all (-D) of the first file given by 
#invoker, but only prints out the ".text" section (-j .text) (only section
#that matters in almost any compiled program...

objdump -Dj .text $1 > $1.ltdis.x86_64.txt


#Check that $1.ltdis.x86_64.txt is non-empty
#Continue if it is, otherwise print error and eject

if [ -s "$1.ltdis.x86_64.txt" ]
then
        echo "Disassembly successful! Available at: $1.ltdis.x86_64.txt"

        echo "Ripping strings from binary with file offsets..."
        strings -a -t x $1 > $1.ltdis.strings.txt
        echo "Any strings found in $1 have been written to $1.ltdis.strings.txt with file offset"



else
        echo "Disassembly failed!"
        echo "Usage: ltdis.sh <program-file>"
        echo "Bye!"
fi

```

static:
```
 HH/lib64/ld-linux-x86-64.so.2GNUGNU'}���3Z���fB��
                                                  �= 
                                                     Y h "libc.so.6puts__cxa_finalize__libc_start_mainGLIBC_2.2.5_ITM_dere � � � � � � H�H��__gmon_start___ITM_registerTMCloneTableu▒i    1�
 H��t��H���5�
 �%�
 @�%�
 h������%�
H�=�����^H��H���PTL��H�
 �DH�=�
 UH��
 H9�H��tH�Z
]��f.�]�@f.�H�=�
 H�5�
 UH)�H��H��H��H��?H�H��t▒H�!
 H��t
     ]��f�]�@f.��=I
 u/H�=�  UH��t
����H����!    H�=�       �
 ]����fDUH��]�f���UH��H�=�������]�f.�DAWAVI��AUATL�%F UH�-F SA��I��L)�H�H���W���H��t 1��L��L��D��A��H��H9�u�H�[]A\A]A^A_Ðf.���H�H��Oh hai! Wait what? A flag? Yes, it's around here somewhere!8����������
                                                                               ���T����<��������,zRx
                                                                                                   ����+zRx
                                                                                                          $P��� F▒J
                                                                                                                   �?▒;*3$RDH��\J���A�C
D|P���eB�B▒�E �B(�H0�H8�M@r8A0A(B B▒B�x���0�
���o�`�                                     �
�
 picoCTF{d15a5m_t34s3r_f5aeda17}GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.08Tt��`�
�
 �
 �  ▒@ ��
 �$�� � k  1C@ �Ji v  ���`e�▒H o0+�▒@ �:�@ � �   �"�
                                                    �crtstuff.cderegister_tm_clones__do_global_dtors_auxcompleted.7698__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entrystatic.c__FRAME_END____init_array_end_DYNAMIC__init_array_start__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE___libc_csu_fini_ITM_deregisterTMCloneTableputs@@GLIBC_2.2.5_edata__libc_start_main@@GLIBC_2.2.5__data_start__gmon_start____dso_handle_IO_stdin_used__libc_csu_init__bss_startmain__TMC_END___ITM_registerTMCloneTableflag__cxa_finalize@@GLIBC_2.2.5.symtab.strtab.shstrtab.interp.note.ABI-tag.note.gnu.build-id.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.text.fini.rodata.eh_frame_hdr.eh_frame.init_arr8#TT 1tt$D���o�Nnamic.data.bss.comment
�� � @ @ �0@)▒  p�▒V``�^y▒� 
```


# Stonks

# Get aHead
curl -I http://mercury.picoctf.net:45028 
- -I = ver las cabeceras

# RSA
nos dan n, e y c

RSA:
- Mensaje encriptado (c)= mensaje^e mod n
- Se necesitan dos números primos, p y q
- n (módulo usado) = p * q
- phi = (p-1) * (q-1)
- e es un número coprimo (MCD de los dos = 1) y menor que phi
	- Exponente de la clave pública. 
- e * d mod n = 1
- mensaje desencriptado = c^d mod n 




http://factordb.com/

2434792384523484381583634042478415057961 
650809615742055581459820253356987396346063

`pip install pycryptodome`

```
from Crypto.Util.number import inverse, long_to_bytes

p=2434792384523484381583634042478415057961
q=650809615742055581459820253356987396346063
e=65537
c=964354128913912393938480857590969826308054462950561875638492039363373779803642185

phi = (p-1)* (q-1)

d=inverse(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m))

```

# The numbers
```C
#include <stdio.h> 

int main(){
	int mensaje[22] = {16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14};
        for (int i=0;i<22;i++){
	        char a = 'a' + mensaje[i] - 1;
	        printf("%c", a);
	}
}
//Se podria haber hecho mejor haciendo que no tenga que escribir yo los {}
```

# New Caesar

```python
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
        enc = ""
        for c in plain:
                binary = "{0:08b}".format(ord(c))
                enc += ALPHABET[int(binary[:4], 2)]
                enc += ALPHABET[int(binary[4:], 2)]
        return enc

def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
print(enc)
```

ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih

Desencriptar eso, teniendo en cuenta que encriptaron con lo de python 



```python
import string

LOWERCASE_OFFSET = ord("a")
# EL ALFABETO SOLO TIENE 16 LETRAS
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
        enc = ""
        for c in plain:
			    #Pilla binario del ascii del caracter, 
                binary = "{0:08b}".format(ord(c))
                enc += ALPHABET[int(binary[:4], 2)]
                enc += ALPHABET[int(binary[4:], 2)]
        return enc

#Convierte a base 10 los primeros 4 digitos y pilla el correspondiente en el alfabeto, luego lo mismo con los siguientes

def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
#Comprueba que todos los elementos de key están en el alfabeto (a-p)
assert all([k in ALPHABET for k in key])
#Comprueba que key solo tiene un elemento
assert len(key) == 1

#Hay 16 posiblidades entre las keys

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
print(enc)
```

reverso:

```python
import string

# OBTIENE EL NUMERO ASCII DE A
LOWERCASE_OFFSET = ord("a")
# EL ALFABETO SOLO TIENE 16 LETRAS
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(plain):
        dec=''
        #Saltos de dos en dos
        for c in range(0,len(plain),2):
                b=''
                #Pasa a formato binario lo que hay en alphabet[c]
                b+="{0:b}".format(ALPHABET.index(plain[c])).zfill(4)
                b+="{0:b}".format(ALPHABET.index(plain[c+1])).zfill(4)
                #Pasa a base 10 el numero desde binario y lo pasa a char
                dec+=chr(int(b,2))
        return dec

def unshift(c, k):
        # OBTIENE EL NUMERO ASCII DE C
        t1 = ord(c) - LOWERCASE_OFFSET
        # OBTIENE EL NUMERO ASCII DE LA LLAVE
        t2 = ord(k) - LOWERCASE_OFFSET
        
        return ALPHABET[(t1 - t2) % len(ALPHABET)]


flag="ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"





for key in ALPHABET:
        desc=''
        for i,char in enumerate(flag):
                desc += unshift(char, key[i % len(key)])

        flag_no_b16=b16_decode(desc)
        print(flag_no_b16)


```


# Cesar

El algoritmo de cesar consiste en sumar a todo el mensaje x veces y hacer modulo 26 (numero de letras del abecedario). 

Así, usando key = 3, "a b z" sería "d e c"

Como no conocemos la key, usamos fuerza bruta:

```python
flag = "dspttjohuifsvcjdpoabrkttds"

for key in range (0,26):
        mensaje=''
        for i,char in enumerate(flag):
                mensaje+=chr((ord(flag[i])-key-ord('a'))%26+ord('a'))
        print(mensaje)
```


# Criptografía con imágenes:
```python
# import Image 
from PIL import Image 
# open both photos 
i1 = Image.open('scrambled1.png') 
i2 = Image.open('scrambled2.png') 
# get width and height 
width1, height1 = i1.size 
# open new image 
i3 = Image.new('RGB', (width1, height1)) 
# load the pixels 
pixels = i3.load() 
# loop through all pixels 
for i in range(width1): 
	for j in range(height1): 
		# xor the values 
		x = i1.getpixel((i,j))[0] ^ i2.getpixel((i,j))[0] 
		y = i1.getpixel((i,j))[1] ^ i2.getpixel((i,j))[1] 
		z = i1.getpixel((i,j))[2] ^ i2.getpixel((i,j))[2] 
		# if all white then convert to black 
		if (x,y,z) == (255,255,255): 
			(x,y,z) = (0,0,0) 
		# put the new pixels in place 
		i3.putpixel((i,j), (x,y,z)) 
# save the image 
i3.save("test.png", "PNG")
```



# Morse-code
Abro el archivo en audacity, ver los puntos y - y usar un traductor de morse


# Ataque de frecuencia


# Modulo
```python
lista=[432, 331, 192, 108, 180, 50, 231, 188, 105, 51, 364, 168, 344, 195, 297, 342, 292, 198, 448, 62, 236, 342, 63]

key="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

  

resultado=""

  

def modInverse(A,  M):

    X=1

    for X in range (1,M):

        if ((A*X)%M==1):

            print(X)

            return X

  

for i in lista:

    num = modInverse(i, 41)

    resultado+=key[num-1]

  
  

print(resultado)
```

```python
lista=[128 ,322 ,353, 235, 336 ,73 ,198, 332, 202, 285, 57 ,87 ,262, 221 ,218 ,405 ,335, 101 ,256, 227 ,112 ,140]

  

key="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

  

resultado=""

  

for i in lista:

    num = i%37

    resultado+=key[num]

  
  

print(resultado)
```