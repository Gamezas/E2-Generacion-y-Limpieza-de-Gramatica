import nltk
from nltk import CFG
nltk.download('punkt')

# Definiendo las reglas de la gramatica
grammar = CFG.fromstring("""
                         
S -> NP L NE
NP -> Sujeto NP1
NP1 -> W NP2 | NP2
NP2 -> T NP2 | 
NE -> NP O
L -> Lugar D
O -> OB V
T -> To NP

W -> 'wa'
D -> 'de'
OB -> 'o'
To -> 'to'
Lugar -> 'koen' | 'mise' | 'eki'
V -> 'mimashita' | 'kikimashita'
Sujeto -> 'inu' | 'neko' | 'tori' | 'otokonohito'
""")

# Parser con la gramática definida
parser = nltk.ChartParser(grammar)

# Oración a revisar
sentence = "inu to neko wa koen de otokonohito o mimashita"

# Volverla un token
tokens = sentence.split()

# Parsear la oración
for tree in parser.parse(tokens):
    tree.pretty_print()