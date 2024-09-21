from Basic import Player, Pokemon, PokemonType, Status


class Game:

    def __init__(
        self,
        players: list[Player],
    ):
        """
        初始化游戏，
        :param players: 玩家列表
        """
        self.players: list[Player] = players
        self.rounds: int = 0

    def onRoundStart(self, player: Player):
        self.rounds += 1
        player.onRoundStart()

    def onRoundEnd(self, player: Player):
        player.onRoundEnd()

    def getGame(self):
        return self

    def GameLoop(self):
        while True:
            for player in self.players:
                print(
                    f"第 {self.rounds} 回合, 玩家 {player.name} 出战 {player.onFightPokemon}"
                )
                self.onRoundStart(player)
                print(f"第 {self.rounds} 回合结束")
                self.onRoundEnd(player)

            if self.rounds >= 10:
                break
        print("游戏结束")
