Fecha: 17/09/2024
Nos dan un [código](./custom_encryption.py) y un [texto](./enc_flag) con información para el cifrado. 

Tras leer y comentar el código, entendí que se usa la misma clave para cifrar y descifrar, así que revertí las funciones "dynamic_xor_encrypt" y "encrypt", probándolo en mi [nuevo código](./custom_decryption.py): 

Desgraciadamente, los valores propuestos por el reto no son correctos, así que no pude obtener la flag. Probando con los siguientes valores encontrados en otro writeup, encuentra un flag (que no sirve para enviar la solución): 

```
a = 94
b = 29
message = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]
```