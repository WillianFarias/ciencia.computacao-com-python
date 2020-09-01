segundos = int(input("Informe o valor em segundos: "))

dia = segundos // 86400
seg_restantes = segundos % 86400

horas = seg_restantes // 3600
seg_restantes = seg_restantes % 3600

minutos = seg_restantes // 60
seg_restantes = seg_restantes % 60

print("Dia(s): {}, Hora(s): {}, Minuto(s): {}, Segundo(s): {}".format(dia, horas,
minutos, seg_restantes))
print()
print("bom dia" 'mundo')
