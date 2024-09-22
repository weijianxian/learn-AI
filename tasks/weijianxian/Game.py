from Basic import Player, Pokemon, PokemonType, Status
from utils import *


class Game:
    rounds: int = 0
    players: list[Player] = []

    def __init__(
        self,
        players: list[Player],
    ) -> None:
        """
        初始化游戏，

        :param players: 玩家列表
        """
        self.players: list[Player] = players

    def __GameStart__(self):
        """
        游戏开始
        """
        print(f"[green]{'游戏开始':=^60}[/]")
        for player in self.players:
            print(f"{player.name} 出战 {player.onFightPokemon}。对手是 {player.target}")

    def __GameEnd__(self):
        """
        游戏结束
        """
        raise NotImplementedError("游戏结束")

    def onRoundStart(self):
        """
        回合开始
        """
        self.rounds += 1
        print("")

    def onRoundEnd(self):
        """
        回合结束,进行游戏状态判断
        """
        for player in self.players:
            if player.onFightPokemon.hp <= 0:
                print(f"{player.name} 出战的 {player.onFightPokemon} 已经死亡")
                self.__GameEnd__()

    def getGame(self):
        return self

    def GameLoop(self):

        self.__GameStart__()
        try:
            while True:
                self.onRoundStart()
                for player in self.players:
                    print(
                        f"[green][Round{self.rounds}][/] {player.name} 出战 {player.onFightPokemon}"
                    )
                    player.onRoundStart()
                    player.onRoundEnd()
                self.onRoundEnd()
        except NotImplementedError as e:
            self.__GameEnd__()
