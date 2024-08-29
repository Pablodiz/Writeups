# Lee el fichero
import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

# Define dos listas de caracteres de longitud 40
lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  cur = lookup1.index(char)
  # Añade a out el caracter en la posición (cur-prev)%40 de lookup2
  out += lookup2[(cur - prev) % 40]
  prev = cur


sys.stdout.write(out)
