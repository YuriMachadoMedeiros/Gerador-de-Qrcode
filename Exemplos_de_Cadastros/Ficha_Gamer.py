#importando a biblioteca rich para usar no terminal

from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()

#Criando a classe para guardar os métodos da ficha
class ficha_gamer:
    def __init__(self, nome=[], nickname=[], idade=[], favoritos=[], cont = 0):
        self.nome = nome
        self.nickname = nickname
        self.idade = idade
        self.favoritos = favoritos
        self.cont = cont
        
    def cadastrar_gamer(self):
        
        while True:
            
            self.nome.append(console.input(f'Escreva seu [bold cyan]nome completo[/] aqui: \n'))
            self.nickname.append(str(console.input(f'Escreva seu [bold cyan]nickname[/] aqui: \n')))
            self.idade.append(int(console.input(f'Escreva sua [bold cyan]idade[/] aqui: \n')))
            self.favoritos.append([])
        
            while True:
                self.favoritos[self.cont].append(console.input(f'Escreva um [bold cyan]jogo favorito[/bold cyan] seu aqui: \n'))

                #Verificar continuidade
                continuarjogos = str(console.input('Tens mais jogos favoritos? [[bold green]S[/bold green]/[bold red]N[/bold red]] ')).upper()
                if continuarjogos == 'N':
                    break
            
            continuar = str(console.input('Queres cadastrar outro gamer? [[bold green]S[/bold green]/[bold red]N[/bold red]] ')).upper()
            if continuar == 'N':    
                break
        
            self.cont += 1

    def exibir_ficha(self):
        ficha = Panel(f"[bold cyan]Nome:[/bold cyan] {self.nome}\n"
                      f"[bold cyan]Nickname:[/bold cyan] {self.nickname}\n"
                      f"[bold cyan]Idade:[/bold cyan] {self.idade}\n"
                      f"[bold cyan]Jogos Favoritos:[/bold cyan] {self.favoritos}\n",
                      title="[bold green]Ficha_Gamer[/bold green]",
                      border_style="bright_blue")
        
        for x, valor in enumerate(self.nome):
            print(Panel(f"[bold cyan]Nome:[/bold cyan] {self.nome[x]}\n"
                      f"[bold cyan]Nickname:[/bold cyan] {self.nickname[x]}\n"
                      f"[bold cyan]Idade:[/bold cyan] {self.idade[x]}\n"
                      f"[bold cyan]Jogos Favoritos:[/bold cyan] {self.favoritos[x]}\n",
                      title=f"[bold green]Ficha_Gamer ID #{x + 1}[/bold green]",
                      border_style="bright_blue"))
            
        

gamer = ficha_gamer()

#Cadastrar múltiplos gamers
def main():

    gamer.cadastrar_gamer()

    #Mostrar Ficha
    gamer.exibir_ficha()

main()
