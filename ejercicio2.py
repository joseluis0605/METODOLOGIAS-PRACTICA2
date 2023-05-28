import re

##text = "Lista de matriculas: pp001234-RRR, 1234 RRR, 1234RRR, E-1234RRR, E 1234RRR, E1234RRR"
text= input("")
pattern = r"\b((E( |-|))?\d{4}( |-|)[A-Z]{3})\b"
results = re.findall(pattern, text)
for match in results:
    print(match[0])