import re

#text = "Lista de calles: “C/ Dulcinea, Nº 10, 28936 Calle Dulcinea 10, 28106 Calle Dulcinea N10, 28091\nTe falta Calle Señor Nº30, 37654 veces vas a ganar. Calle Abuñol 30, 28000      Calle Ñoqui 0,  00000     Calle Pepo º1, 00000  Calle Tricky, Nº7, 00001"
text= input("")
pattern = r"\b((C\/|Calle)( | del | de la | Del | De La | De la | de La )([A-ZÑ][a-zñ]+)(,)?\s+(N|n|Nº|nº)?( |)(\d+),\s+(\d{5}))\b"
results = re.findall(pattern, text)
for match in results:
    #print(match)
    cp = match[8]
    n = match[7]
    calle = match[3]
    print(cp+'-'+calle+'-'+n)
