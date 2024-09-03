Fecha: 06/08/2024

Hago nmap, y veo que tiene un servidor http abierto:
```
nmap -sV 172.17.0.2
```

![](Imágenes/Pasted%20image%2020240806152823.png)

Miro el html y veo el siguiente comentario:

![](Imágenes/Pasted%20image%2020240806152424.png)

Usando hydra y el diccionario rockyou.txt, con el usuario Camilo, intentaré meterme en la máquina:
```
hydra -l camilo -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2
```

![](Imágenes/Pasted%20image%2020240806154321.png)

Como vemos, hay un usuario `camilo` con contraseña `password1`

Me conecto por ssh, y ya estamos en la máquina. 

![](Imágenes/Pasted%20image%2020240806154439.png)

Ahora buscaré el correo, ya que como dice el comentario, puede haber algo de valor allí. Antes, uso bash para usar una terminal más cómoda. 

![](Imágenes/Pasted%20image%2020240806154651.png)

Uso esta contraseña para acceder como juan: 

![](Imágenes/Pasted%20image%2020240806155049.png)

Haciendo `sudo -l` descubro que juan puede ejecutar /usr/bin/ruby con permisos de root:

![](Imágenes/Pasted%20image%2020240806155336.png)

En https://gtfobins.github.io/gtfobins/ruby/ encuentro que con el siguiente comando y con permisos de sudo, puedo obtener una shell de root:


![](Imágenes/Pasted%20image%2020240806155732.png)

Y, efectivamente:

![](Imágenes/Pasted%20image%2020240806155759.png)
