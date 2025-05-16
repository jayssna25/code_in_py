class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def cadastro_hora(self, mes, horas):
        if not isinstance(horas, (int, float)) or horas < 0:
            print("Erro: Horas devem ser um número não negativo.")
            return
        if mes not in self.horas:
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            print("Erro: Valor do salário por hora deve ser um número não negativo.")
            return
        if mes not in self.salario_hora:
            self.salario_hora[mes] = valor

    def calcula_salario(self, mes):
        if mes not in self.horas or mes not in self.salario_hora:
            print(f"Erro: Dados de horas ou salário-hora inexistentes para o mês de {mes}.")
            return None
        else:
            return self.horas[mes] * self.salario_hora[mes]

    def __repr__(self):
        return (f"Funcionário: {self.nome}\n"
                f"Email: {self.email}\n"
                f"Horas por mês: {self.horas}\n"
                f"Salário por hora: {self.salario_hora}")

# Exemplo de uso
funcionario1 = Funcionario("Jair Bolsonaro", "jair.b@email.com")
funcionario1.cadastro_hora("Janeiro", 160)
funcionario1.cadastro_salario_hora("Janeiro", 25.50)
salario_janeiro = funcionario1.calcula_salario("Janeiro")
if salario_janeiro is not None:
    print(f"Salário de Janeiro: R$ {salario_janeiro:.2f}")

funcionario1.cadastro_hora("Fevereiro", 150)
funcionario1.cadastro_salario_hora("Fevereiro", 28.00)

print(funcionario1)
