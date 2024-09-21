import random as rd

from Game import Game
from Player import Player
from Pokemon import Bulbasaur, Charmander, Pikachu, PokemonList, Squirtle
from utils import *  # 导入自定义的print函数

print(
    """\
[green],-.----.                                                                             [/][red]                        [/] 
[green]\    /  \                    ,-.                       ____                          [/][red]   ,----..              [/] 
[green]|   :    \               ,--/ /|                     ,'  , `.                        [/][red]  /   /   \             [/] 
[green]|   |  .\ :    ,---.   ,--. :/ |                  ,-+-,.' _ |    ,---.         ,---, [/][red] |   :     :     ,---.  [/] 
[green].   :  |: |   '   ,'\  :  : ' /                ,-+-. ;   , ||   '   ,'\    ,-+-. /  |[/][red] .   |  ;. /    '   ,'\ [/] 
[green]|   |   \ :  /   /   | |  '  /       ,---.    ,--.'|'   |  ||  /   /   |  ,--.'|'   |[/][red] .   ; /--`    /   /   |[/] 
[green]|   : .   / .   ; ,. : '  |  :      /     \  |   |  ,', |  |, .   ; ,. : |   |  ,"' |[/][red] ;   | ;  __  .   ; ,. :[/] 
[green];   | |`-'  '   | |: : |  |   \    /    /  | |   | /  | |--'  '   | |: : |   | /  | |[/][red] |   : |.' .' '   | |: :[/] 
[green]|   | ;     '   | .; : '  : |. \  .    ' / | |   : |  | ,     '   | .; : |   | |  | |[/][red] .   | '_.' : '   | .; :[/] 
[green]:   ' |     |   :    | |  | ' \ \ '   ;   /| |   : |  |/      |   :    | |   | |  |/ [/][red] '   ; : \  | |   :    |[/] 
[green]:   : :      \   \  /  '  : |--'  '   |  / | |   | |`-'        \   \  /  |   | |--'  [/][red] '   | '/  .'  \   \  / [/] 
[green]|   | :       `----'   ;  |,'     |   :    | |   ;/             `----'   |   |/      [/][red] |   :    /     `----'  [/] 
[green]`---'.|                '--'        \   \  /  '---'                       '---'       [/][red]  \   \ .'              [/] 
[green]  `---`                             `----'                                           [/][red]   `---`                [/] 
[green]欢迎来到宝可梦世界[/]"""
)


def main():
    for index, pokemon in enumerate(PokemonList):
        print(
            f"[green]{index}. {pokemon.name}[/]\t[red]hp: {pokemon.hp}[/]\t[cyan]攻击: {pokemon.attack}[/]\t[yellow]防御: {pokemon.defense}[/]"
        )

    index = int(input("[green]请输入你选择的宝可梦编号:[/]"))

    user = Player("你：", PokemonList[index], PokemonList)
    computer = Player("电脑：", PokemonList[rd.randint(0, 3)], PokemonList)

    game = Game([user, computer])
    game.GameLoop()


if __name__ == "__main__":
    main()
