Introduzco la salida del comando en netcat.txt y: 
```python
fichero = open('netcat.txt', 'r').read().replace(' ', '')

lista = fichero.split('\n')

resultado = ""

for i in lista:
    try:
        resultado+=chr(int(i))
    except:
        pass
print(resultado)
```