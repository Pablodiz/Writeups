18-10-2025

Vemos que no tiene particiones
```
fdisk -l disko-3.dd
``` 

Lo montamos 
```
sudo mount disko-3.dd /mnt/d3
```

Solo hay una carpeta log, miramos el contenido
![](Informatica/Hacking/Writeups/picoCTF/Forensics/Medium/Imágenes/DISKO3.png)

Destaca flag.gz:
```
sudo gzip -d flag.gz
cat flag
```