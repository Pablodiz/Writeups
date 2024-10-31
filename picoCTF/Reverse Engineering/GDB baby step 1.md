Se busca encontrar el valor en decimal del registro eof the main.

Usando gdb, que es lo que sugiere el título: 

```
gdb -q debugger0_a
set disassembly-flavor intel
disassemble main
```

![](Imágenes/Pasted%20image%2020241031022004.png)

Paso eso desde hexadecimal y ya lo tengo:
```python
print(int("0x86342",16))
```

# GDB baby step 2
![](Imágenes/Pasted%20image%2020241031023616.png)

