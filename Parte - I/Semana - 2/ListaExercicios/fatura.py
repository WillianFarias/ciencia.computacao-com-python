nome = input("Digite o nome do cliente: ")
dia_vencimento = input("Digite o dia de vencimento: ")
mes_vencimento = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

print("Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada."
.format(nome, dia_vencimento, mes_vencimento, valor))