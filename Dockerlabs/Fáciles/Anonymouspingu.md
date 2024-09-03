Comienzo haciendo el escaneo, encontrando ftp en el puerto 21 y un apache en el 80, siendo ninguna de las dos versiones vulnerable según seachsploit. 
```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.2 -oN scan
```

```
wget -r ftp://172.17.0.2/images
```

#TODO ACABAR