from rich import print
from rich.panel import Panel

class Funcionario:
    def __init__(self, nome='', idade=0, setor='', cargo='', salario=0.0):
        self.nome = nome
        self.idade = idade
        self.setor = setor
        self.cargo = cargo
        self.salario = salario
        
    def cadastrar_funcionario(self):
        self.nome = str(input("Digite o nome do funcionário: "))
        self.idade = int(input("Digite a idade do funcionário: "))
        self.setor = str(input("Digite o setor do funcionário: "))
        self.cargo = str(input("Digite o cargo do funcionário: "))
        self.salario = float(input("Digite o salário do funcionário: "))
        
    def exibir_dados(self):
        caixa = Panel(f"[bold cyan]Nome:[/bold cyan] {self.nome}\n"
                      f"[bold cyan]Idade:[/bold cyan] {self.idade}\n"
                      f"[bold cyan]Setor:[/bold cyan] {self.setor}\n"
                      f"[bold cyan]Cargo:[/bold cyan] {self.cargo}\n"
                      f"[bold cyan]Salário:[/bold cyan] R$ {self.salario:.2f}",
                      title="[bold green]Dados do Funcionário[/bold green]",
                      border_style="bright_blue")
        print(caixa)
funcionario = Funcionario()
funcionario.cadastrar_funcionario()
funcionario.exibir_dados()

        

