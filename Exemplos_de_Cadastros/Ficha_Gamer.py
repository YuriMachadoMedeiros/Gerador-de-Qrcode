#importando a biblioteca rich para usar no terminal

from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()

#Criando a classe para guardar os métodos da ficha
class ficha_gamer:
    def __init__(self, nome='', nickname='', idade=0, favoritos=[]):
        self.nome = nome
        self.nickname = nickname
        self.idade = idade
        self.favoritos = favoritos

    def cadastrar_gamer(self):
        self.nome = console.input(f'Escreva seu [bold cyan]nome completo[/] aqui: \n')
        self.nickname = str(console.input(f'Escreva seu [bold cyan]nickname[/] aqui: \n'))
        self.idade = int(console.input(f'Escreva sua [bold cyan]idade[/] aqui: \n'))
        while True:
            self.favoritos.append(console.input(f'Escreva um [bold cyan]jogo favorito[/bold cyan] seu aqui: \n'))

            #Verificar continuidade
            continuarjogos = str(console.input('Tens mais jogos favoritos? [[bold green]S[/bold green]/[bold red]N[/bold red]] ')).upper()
            if continuarjogos == 'N':
                break

    def exibir_ficha(self):
        ficha = Panel(f"[bold cyan]Nome:[/bold cyan] {self.nome}\n"
                      f"[bold cyan]Nickname:[/bold cyan] {self.nickname}\n"
                      f"[bold cyan]Idade:[/bold cyan] {self.idade}\n"
                      f"[bold cyan]Jogos Favoritos:[/bold cyan] {self.favoritos}\n",
                      title="[bold green]Ficha_Gamer[/bold green]",
                      border_style="bright_blue")
        print(ficha)

gamer = ficha_gamer()

#Cadastrar múltiplos gamers
def main():

    gamer.cadastrar_gamer()

    #Mostrar Ficha
    gamer.exibir_ficha()

main()
