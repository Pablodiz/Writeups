Parece típico lenguaje de programación de broma (al repetir tantas veces palabras similares al principio). 

```
Pico's a CTFFFFFFF
my mind is waitin
It's waitin

Put my mind of Pico into This
my flag is not found
put This into my flag
put my flag into Pico


shout Pico
shout Pico
shout Pico

My song's something
put Pico into This

Knock This down, down, down
put This into CTF

shout CTF
my lyric is nothing
Put This without my song into my lyric
Knock my lyric down, down, down

shout my lyric

Put my lyric into This
Put my song with This into my lyric
Knock my lyric down

shout my lyric

Build my lyric up, up ,up

shout my lyric
shout Pico
shout It

Pico CTF is fun
security is important
Fun is fun
Put security with fun into Pico CTF
Build Fun up
shout fun times Pico CTF
put fun times Pico CTF into my song

build it up

shout it
shout it

build it up, up
shout it
shout Pico  
````

Busco "shout knock put programming language" y encuentro que hay un lenguaje llamado rockstar. Encuentro un ejecutador online y me devuelve una línea de números que parecen ASCII. Hago un script python que lo imprima y obtengo el flag

```python
lista = [114 
,114
,114
,111
,99
,107
,110
,114
,110
,48
,49
,49
,51
,114]


resultado = ""

for i in  lista:
	resultado+=chr(i)

print(resultado)
```

En 1_wanna_b3_a_r0ck5tar, la "letra" es: 
```
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"                
Listen to the rhythm
If the rhythm without Music is nothing
Tommy is rockin guitar
Shout Tommy!                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!                 
Tommy is playing rock           
Scream Tommy!       
They are dazzled audiences                  
Shout it!
Rock is electric heaven                     
Scream it!
Tommy is jukebox god            
Say it!                                     
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"                 
Break it down 
```

Pide una entrada. Como no sé qué puede querer, investigo y encuentro un paquete de python que me permite traducir:
https://pypi.org/project/rockstar-py/

```bash
 rockstar-py -i lyrics.txt -o lyrics.py
```


```python
Rocknroll = True
Silence = False
a_guitar = 10
Tommy = 44
Music = 170
the_music = input()
if the_music == a_guitar:
    print("Keep on rocking!")
    the_rhythm = input()
    if the_rhythm - Music == False:
        Tommy = 66
        print(Tommy!)
        Music = 79
        Jamming = 78
        print(Music!)
        print(Jamming!)
        Tommy = 74
        print(Tommy!)
        They are dazzled audiences
        print(it!)
        Rock = 86
        print(it!)
        Tommy = 73
        print(it!)
        break
        print("Bring on the rock!")
        Else print("That ain't it, Chief")
        break

```

Para que el programa continúe:
- the_music = a_guitar = 10   -> Introducir 10
- the_rythm - 170 = false = 0 -> Introducir 170

Arreglando un poco el código consigo arreglar un poco la lista salvo una letra, que por contexto se que es la O: 

```python
Rocknroll = True
Silence = False
a_guitar = 10
Tommy = 44
Music = 170
the_music=10
if the_music == a_guitar:
    print("Keep on rocking!")
    the_rhythm = 170
    if the_rhythm - Music == False:
        Tommy = 66
        print(Tommy)
        Music = 79
        Jamming = 78
        print(Music)
        print(Jamming)
        Tommy = 74
        print(Tommy)
        #print(it)
        Rock = 86
        print(Rock)
        Tommy = 73
        print(Tommy)
        print("Bring on the rock!")
    else:
        print("That ain't it, Chief")

lista = [66
,79
,78
,74
,86
,73]


resultado = ""

for i in  lista:
	resultado+=chr(i)

print(resultado)
```

![](Imágenes/Pasted%20image%2020241031014153.png)

