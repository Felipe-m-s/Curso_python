# Exemplo 4
mensalidade = 100.00;

valor_pago = float(input("Digite o valor pago: "))

if (valor_pago < mensalidade):
    diferenca = mensalidade - valor_pago
    print (f"Faltou R$ {diferenca}. Pontando há uma mulda de R$ {diferenca*0.1}. Valor total: {diferenca+diferenca*0.1}")
elif (valor_pago > mensalidade):
    print("Valor recebido à mais. Troco: R$ {valor_pago-mensalidade}")
else:
    print("Obrigado!!")

print("Tenhas um bom treino!")