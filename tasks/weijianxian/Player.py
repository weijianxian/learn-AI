from Basic import Player, Pokemon
from utils import *


class Player(Player):

    def __str__(self) -> str:
        return self.name

    def onRoundStart(self):
        """
        回合开始
        """
        self.onFightPokemon.onRoundBegin()
        index = question(
            "[green][1][/] 战斗 [green][2][/] 使用技能:",
            ["1", "2"],
        )

        if index == "1":
            result = self.onFightPokemon.fight(self.target)
            print(result[2])
            print(
                f"{self.target.onFightPokemon} 剩余生命值: {self.target.onFightPokemon.hp}"
            )

        else:
            self.onFightPokemon.skill(self.target)

    def onRoundEnd(self):
        """
        回合结束
        """
        self.onFightPokemon.onRoundEnd()


class AI(Player):

    def onRoundStart(self):
        """
        回合开始
        """
        result = self.onFightPokemon.fight(self.target)
        print(result[2])
        print(
            f"{self.target.onFightPokemon} 剩余生命值: {self.target.onFightPokemon.hp}"
        )

    def onRoundEnd(self):
        """
        回合结束
        """
        self.onFightPokemon.onRoundEnd()

    def switchPokemon(self, pokemon: Pokemon):
        """
        切换宝可梦
        """
        if pokemon not in self.pokemons:
            raise ValueError("宝可梦不在列表中")

        self.onFightPokemon = pokemon
