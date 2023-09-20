# Explicação de classe Python
<br><br>
Uma explicação das senhas e dos comandos no comentário de como é criada uma classe em Python
<br><br>
## Explicação
<br>
• <code>class Pessoa:</code>: Inicia a definição da classe Pessoa.

• <code>def __init__(self, nome, cpf, email):</code>: Define o método construtor da classe Pessoa. O método <code>__init__</code>(dois underline antes e depois) é chamado automaticamente quando uma nova instância da classe é criada. Ele inicializa os atributos da pessoa com os valores fornecidos (nome, cpf e email).

• <code>self.nome = nome</code>: Cria o atributo "nome" da instância e atribui a ele o valor passado como argumento.

• <code>self.cpf = cpf</code>: Cria o atributo "cpf" da instância e atribui a ele o valor do CPF passado como argumento.

• <code>self.email = email</code>: Cria o atributo "email" da instância e atribui a ele o valor do e-mail passado como argumento.

• <code>def exibir_informacoes(self):</code>: Define um método chamado "exibir_informacoes" que exibirá os dados da pessoa.

• <code>print("Nome:", self.nome)</code>: Exibe o nome da pessoa.

• <code>print("CPF:", self.cpf)</code>: Exibe o CPF da pessoa.

• <code>print("E-mail:", self.email)</code>: Exibe o e-mail da pessoa.

• <code>pessoa1 = Pessoa("Leonardo Stella", "123.456.789-00", "leonardo@lesttech.com")</code>: Cria uma instância da classe Pessoa com os valores fornecidos para nome, CPF e e-mail.

• <code>pessoa1.exibir_informacoes()</code>: Chama o método "exibir_informacoes" para exibir as informações da pessoa criada.