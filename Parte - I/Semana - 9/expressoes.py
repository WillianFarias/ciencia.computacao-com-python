import re

texto = "Foda-se. Otarios! se? liga babacas, vocs sao otarios"

teste = re.split(r'[.!?]+', texto)

print(teste)