18-10-2025

![](Informatica/Hacking/Writeups/picoCTF/Forensics/Easy/Imágenes/Corrupted%20file.png)

Vemos que es un jpg corrupto. Debería empezar con FF D8 FF

Con `hexedit`, edito directamente los caracteres hexadecimales, y cierro con Control+X.

![](Informatica/Hacking/Writeups/picoCTF/Forensics/Easy/Imágenes/Corrupted%20file-1.png)

```
tesseract file.jpg salida.txt
```

