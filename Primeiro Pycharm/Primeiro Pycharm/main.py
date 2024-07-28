from contasbanco import CartaoCredito, ContaCorrente
from agencias import AgenciaPremium, AgenciaComum, AgenciaVirtual

#Programa

    #Criando contas
conta_lemos = ContaCorrente('Gabriel', '111.222.333-00', 45865, 4944)

conta_marley = ContaCorrente('Marley',111111,6666,981)

    #Conta do cartão de crédito
cartao_gabriel = CartaoCredito('Messi', conta_lemos)


cartao_gabriel.senha = "6214"






agencia_super = AgenciaPremium(457502, 785758)




