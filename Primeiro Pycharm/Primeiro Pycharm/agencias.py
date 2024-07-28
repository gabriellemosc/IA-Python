from random import randint

class Agencias():

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.emprestimos = []
        self.caixa = 0

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('O valor do caixa está abaixo. Valor em caixa R${:,.2f}'.format(self.caixa))
        else:
            print('O valor do Caixa está de acordo. Valor R${:,.2f}'.format(self.caixa))


    def realizar_emprestimo(self, valor, cnpj, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cnpj, juros))
            self.caixa -= valor
        else:
            print('O empréstimo não será possível. Valor do Caixa abaixo')


    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencias):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 100)
        self.caixa = 15000000
        self.paypal = 0

    def depositar_paypal(self, valor):
        if self.caixa < valor:
            print('Valor em caixa menor que o solicitado. Valor  solicitado R${:,.2f}. Valor em caixa {:,.2f}'.format(valor, self.caixa))
        else:
            self.caixa -= valor
            self.paypal += valor



    def sacar_pay_pal(self, valor):
        if self.paypal < valor:
            print('Valor em caixa menor que o solicitado. Valor solicitado R${:,.2f}. Valor em caixa {:,.2f}'.format(valor, self.paypal ))
        else:
            self.caixa += valor
            self.paypal -= valor

class AgenciaComum(Agencias):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 5000000

class AgenciaPremium(Agencias):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000


    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
           super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não tem patrimonio suficiente para entrar na agência Premium')


if __name__ == '__main__':

    agencia1 = Agencias(11111, 1000000000, 100)

    agencia_virtual = AgenciaVirtual('wwww.agenciavirtual.com', 445590, 467 )

    agencia_comum = AgenciaComum(69785, 4514)

    agencia_premium = AgenciaPremium(445544, 1200000000)


    agencia_premium.adicionar_cliente('Daniel',15459494, 1000000000)

    print(agencia_premium.clientes)


