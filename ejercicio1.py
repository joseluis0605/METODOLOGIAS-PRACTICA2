import re

#text = "Estamos en el año 2023, el año pasado fue 2022, el primer año fue el 0000, y un año no seria 20199, 3333."
text= input("")
pattern = r"\b\d{4}\b"
results = re.findall(pattern, text)
for match in results:
    print(match)
