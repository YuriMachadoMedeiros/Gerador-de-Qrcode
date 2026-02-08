# 400g por pessoa
# R$82,40/KG

#Importando as bibliotecas necessárias para apresentação
from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console

#Criando a classe para guardar os métodos do churrasco
class churrasco:

    #Construtor da classe onde abriga todos os atributos
    def __init__(self, titulo = '', convidados = 0, quilos = 0.0, valor = 0.0):
        self.titulo = titulo
        self.convidados = convidados
        self.quilos = quilos
        self.valor = valor
    
    #Definir os atributos do churrasco
    def definir_atributos(self):
        self.titulo = str(input(f'Nome do churrasco: '))
        self.convidados = int(input(f'Quantos convidados irão? '))

    #Calcular os dados do churrasco
    def dados_churrasco(self):
        self.quilos = self.convidados * 0.4
        self.valor = self.quilos * 82.40

    #Exibir os dados do churrasco
    def exibir_dados(self):
        painel = Panel(f"Analisando [bold green]{self.titulo}[/bold green] com [bold red] {self.convidados}[/bold red] convidados.\n"
                       f"[bold cyan]Sendo o quilo da carne R$82,40 e cada convidado comendo 0,4KG.[/bold cyan]\n"
                       f"Serão necessários então [bold cyan]{self.quilos}KG[/bold cyan] de carne.\n"
                       f"Ficando [bold cyan]R${self.valor:.2f}[/bold cyan] no total.\n",
                       title="[bold green]Churrasco[/bold green]",
                       border_style="bright_blue")

        print(painel)

#Criando o objeto do churrasco
churrasco = churrasco()

#Definir os atributos, calcular os dados e exibir o resultado do churrasco
def main():

    churrasco.definir_atributos()
    churrasco.dados_churrasco()
    churrasco.exibir_dados()

#Executar o programa
main()
