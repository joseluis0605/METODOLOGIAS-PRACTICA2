import re

text = input()
pattern   = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\s+(\w+)\s+\d+\s+---\s+\[(\w+)\]\s+(?:\w+\.)*(\w+)\s+:\s+(.*)"
results = re.findall(pattern, text)
for match in results:
    print('"'+match[0]+'"'+","+'"'+match[1]+'"'+","+'"'+match[2]+'"'+","+'"'+match[3]+'"')