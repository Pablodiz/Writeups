import sys
chars = ""
from fileinput import input
for line in input():
  chars += line



lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  cur2 = lookup2.index(char)
  # Añade a out el caracter en la posición (cur-prev)%40 de lookup2
  out += lookup1[(cur2 + prev) % 40]
  prev = cur2 + prev

sys.stdout.write(out)