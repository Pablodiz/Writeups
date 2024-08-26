Con exiftool, veo una línea que parece estar en base64:
`Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==`

Descifrando usando la herramienta base64, obtengo:
```
echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==" | base64 -d
picoCTF{ME74D47A_HIDD3N_6a9f5ac4}
```
Fecha: 01/08/2024