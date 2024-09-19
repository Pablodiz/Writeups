Usando xxd, una herramienta que muestra los bytes en hexadecimal de una archivo y su decodificación en ASCII, al final del fichero se encuentra el flag: 

```
xxd garden.jpg
```
![](../../../Dockerlabs/Fáciles/Imágenes/Pasted%20image%2020240801044959.png)
```
"picoCTF{more_than_m33ts_the_3y3657BaB2C}"
```

Investigando soluciones, veo que hay un comando que puede ser incluso más útil: `strings`
```
strings garden.jpg | grep pico
Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"
```

Fecha: 01/08/2024