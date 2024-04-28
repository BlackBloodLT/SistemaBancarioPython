class class_conta:
    def __init__(self, saldo=0, limite=500, extrato='', numero_saques=0):
        self.saldo = saldo
        self.limite = limite
        self.extrato = extrato
        self.numero_saques = numero_saques
        self.LIMITE_SAQUES = 3