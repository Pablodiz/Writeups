Fecha: 31/07/2024

Me indican una máquina y  2 puertos: 
- Uno que está "filtrando" información.
- Uno para conectarme a la aplicación.
Uso el comando `nc` a la instancia y puerto que "filtra información"
Obtengo la siguiente información:
```
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234
```
Me conecto por netcat (`nc`) al otro puerto, e introduzco -> My_Passw@rd_@1234 como contraseña. 

Me pregunta por la mayor conferencia de ciber en el mundo, que es -> DEF CON

El primer hacker en la historia, conocido por hacer llamadas telefónicas gratis ("phreaking") -> JOHN DRAPER

De aquí obtengo acceso a la shell:
- Haciendo ls en /home/player (mi carpeta de usuario) encuentro dos text-files, irrelevantes.
- Viendo los archivos en /root, encuentro que script.py tiene permisos de lectura universales. Una de las líneas del archivo es la siguiente:
```
with open("/home/player/banner", "r") as f:
        print(f.read())
```
- Pensé en copiar el archivo /root/flag.txt en /home/player/banner para que al conectarme por siguiente vez al puerto me diga directamente el contenido de este archivo, pero sin permisos no puedo así que creé un link simbólico al flag en /home/player/banner. 
```
ln -s /root/flag.txt /home/player/banner
```
- El script se ejecuta con las credenciales de root al iniciar la máquina, por lo que podrá leer el contenido del archivo /root/flag.txt, al que apunta el link simbólico, y nos lo imprimirá por pantalla
``` 
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_ed6f9c71}
```

