![[Pasted image 20240801024851.png]]
Recibo esta lista de códigos hexadecimales. Sustituyo todos los " 0x" por "" usando visualstudio y lo convierto a un string. Obtengo los bytes desde el string y los decodifico a ASCII, usando python: 
```
string = "7069636f4354467b34356331315f6e305f717533353731306e355f316c6c5f743331315f79335f6e305f6c3133355f34343564343138307d"

byte_string = bytes.fromhex(string)

print(byte_string.decode("ASCII"))
```


Fecha: 01/08/2024
