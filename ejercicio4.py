import re

##text = "Lista de correos: iiiiii.lozanoo.2015@alumnos.urjc.es isaac.lozano@urjc.es"
text= input("")
pattern = r"\b(([a-z]+)\.([a-z]+)(@urjc\.es)|[a-z]{1,2}\.([a-z]+)\.(\d{4})(@alumnos\.urjc\.es))\b"
results = re.findall(pattern, text)
for match in results:
    #print(match)
    if match[6] == '@alumnos.urjc.es':
        apellido = match[4]
        anio = match[5]
        print('alumno '+apellido+' matriculado en '+anio)
    else:
        nombre = match[1]
        apellido = match[2]
        print('profesor '+nombre+' apellido '+apellido)
