from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
console = Console()

#Criando a classe para guardar os métodos do produto
class produto:

    #Construtor da classe onde abriga todos os atributos
    def __init__(self, nome = [], valor = [], codigo=[], cont = 0):

        self.nome = nome
        self.valor = valor
        self.codigo = codigo
        self.cont = cont

    def cadastrar(self):

        while True:
            self.nome.append(console.input(f'[bold red]Nome do Produto[/]: \n'))
            self.valor.append(float(console.input(f'[bold red]Valor do Produto[/]: \n')))
            self.codigo.append(console.input(f'[bold red]Código do Produto[/]: \n'))

            continuar = console.input(f'Deseja adicionar mais um Produto? [S/N]\n ').upper()
            if continuar == 'N':
                break

            self.cont += 1

    def exibir_produto(self):
        
        tabela = Table(title="Tabela de Preços")

        tabela.add_column("Produto", justify="left", style="cyan", no_wrap=True)
        tabela.add_column("Preço", justify="center", style="green")
        tabela.add_column("Código", justify="center", style="magenta")
                
        for x, valor in enumerate(self.nome):
            tabela.add_row(self.nome[x], f"R${self.valor[x]:.2f}", self.codigo[x])
        
        console.print(tabela)
                        

produto = produto()

def main():
    produto.cadastrar()

    produto.exibir_produto()

main()
