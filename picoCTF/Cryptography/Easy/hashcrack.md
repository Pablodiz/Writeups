2025-11-10

```
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
```

Cada vez que se resuelve uno de los hashes, nos devuelve otro. Para resolver el problema:
- `hashid <hash>` <- obtenemos las funciones hash que podrían producir esta salida. El primero fue MD5, el segundo SHA1 y el tercero SHA256
- `hashcat -m {0,100,1400} hash.txt /usr/share/wordlists/rockyou.txt`

Una vez resuelto cada uno de esos hashes, obtuve el flag.