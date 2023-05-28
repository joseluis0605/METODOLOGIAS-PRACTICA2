import re

##= "asrsdfsadf12e4-12-24dadfbvijndf 9999-11-22asrsdfsadf\n 1234-12-24 dadfbvijndf \n9999-11-22 "
text=input("")
pattern = r"\b(\d{4}-\d{2}-\d{2})\b"
results = re.findall(pattern, text)
for match in results:

    anio, mes, dia = match.split("-")
    fechaBuena = dia+"."+mes+"."+anio
    fraseBuena = re.sub(match, fechaBuena, text)
    text = fraseBuena
print(text)

