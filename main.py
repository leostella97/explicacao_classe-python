# Definindo a classe Pessoa
class Pessoa:
    # Método construtor da classe, onde inicializamos os atributos da pessoa, sempre começa com o 'self'
    def __init__(self, nome, cpf, email):
        self.nome = nome  # Atributo para armazenar o nome da pessoa
        self.cpf = cpf    # Atributo para armazenar o CPF da pessoa
        self.email = email  # Atributo para armazenar o e-mail da pessoa

    # Método para exibir informações da pessoa
    def exibir_informacoes(self): # def = definir função, 'def' é de define
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("E-mail:", self.email)

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Leonardo Stella", "123.456.789-00", "leonardo@lesttech.com")

# Chamando o método para exibir as informações da pessoa
pessoa1.exibir_informacoes()
