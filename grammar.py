import nltk
from nltk import CFG
nltk.download('punkt')

# Definiendo las reglas de la gramatica
grammar = CFG.fromstring("""

S -> NP
NP -> NP NE | NP W | NP L | T NP | Sujeto
NE -> L NE | NP O
L -> L D | Lugar
O -> O V | OB
T -> NP To

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