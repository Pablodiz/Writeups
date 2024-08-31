Fecha: 31/08/2024
El reto pide que nos conectemos por netcat a cierta dirección y puerto, devolviéndonos lo siguiente: 
![](imágenes/Pasted%20image%2020240831154634.png)

Usando un conversor de morse y editando un poco la salida, obtenemos el flag:
 ```python
 from morse3 import Morse

mensaje = ".--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ...-- ----. ----- ..--- ----- .---- ----. ..... .---- ----. } "

herramienta = Morse(mensaje)
 ```

Salida: `picoctfm0rs3c0d31sfun3902019519`
Tras editar: `picoCTF{m0rs3c0d31sfun3902019519}`