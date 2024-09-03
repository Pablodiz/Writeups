#TODO acabarla

Comienzo con un nmap. Hay un ssh en el 22 y un Apache en el 80, ninguno de ellos vulnerable.

```
sudo nmap -p- -sS -sC -sV --min-rate 5000 -n -Pn 172.17.0.3 -oN scan
```  

Inspeccionando la página no encuentro nada, así que haré fuzzing:
```
feroxbuster -u http://172.17.0.3 -x php -x html -x txt -x js -x py -w /usr/share/wordlists/directory-list-2.3-medium.txt -o fuzzing --threads 300  
```

Encuentro varios directorios: 