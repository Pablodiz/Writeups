18-10-2025

Tengo un archivo de log en el que aparecer hay algo encodeado


```bash
base64 -d logs.txt  > image.jpg
```


![](Informatica/Hacking/Writeups/picoCTF/Forensics/Easy/Imágenes/Flag%20in%20Flame.png)

7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F37383265353563397D

```bash
tesseract image.jpg salida.txt
```

```
echo -n "7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F37383265353563397D" | base16 -d
```

