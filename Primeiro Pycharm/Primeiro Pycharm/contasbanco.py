from datetime import datetime
import  pytz
from random import  randint
class ContaCorrente:
    """
    Cria um objeto da Classe ContaCorrente e gerenciar essas contas.

    Atributos:
    Nome do Cliente
    CPF do Cliente
    Agência do cliente
    Número de Conta do Cliente
    Saldo da Conta
    Limite de Transações
    Histórico de Transcações

    """

    @staticmethod
    def data_hora():
        fuso_Br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_Br)
        return horario_br.strftime('%d/%m/%Y, %H:%M:%S')

    #Caractéricas da Classe
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._transacao = []
        self._agencia = agencia
        self._nu_conta = num_conta
        self.cartoes = []


#Métodos
    def consultar_saldo(self):
        print("O seu saldo atual é de R${:,.2f}".format(self._saldo))

    def _limite_conta(self):
        self._limite = -1000
        return  self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacao.append((-valor, self._saldo, ContaCorrente.data_hora()))


    def depositar_dinheiro(self, valor):
        self._saldo += valor
        self._transacao.append((valor, self._saldo, ContaCorrente.data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite do cheque especial é de {:,.2f}'.format(self._limite_conta()))

    def consultar_historico(self):
        print('Histórico de transcaoes')
        print('Valor, Saldo, data e hora')
        for transferencia in self._transacao:
            print(transferencia)

    def transferir_dinheiro(self, valor, conta_destino):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem recursos para essa transação')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacao.append((-valor, self._saldo, ContaCorrente.data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacao.append((valor, conta_destino._saldo, ContaCorrente.data_hora()))


class CartaoCredito:

    @staticmethod
    def data_hora():
        fuso_Br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_Br)
        return horario_br

    def __init__(self, nome, conta_corrente):
        self.numero_cartao = randint(1000000000000000, 9999999999999999)
        self.data_validade = '{}/{}'.format(CartaoCredito.data_hora().month, CartaoCredito.data_hora().year + 4)
        self.limite = 1000
        self.cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9),randint(0,9))
        self.nome = nome
        self.conta_corrente = conta_corrente
        self._senha = "1234"
        conta_corrente.cartoes.append(self)

    #Consultar
    @property
    def senha(self):
        return self._senha

    #Modificandp senha
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova Senha Inválida!')







