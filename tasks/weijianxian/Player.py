from Basic import Pokemon


class Player:

    def __init__(
        self,
        name: str,
        fightPokemon: Pokemon,
        pokemons: list[Pokemon],
    ):
        self.name: str = name  # 玩家名称
        self.onFightPokemon: Pokemon = fightPokemon  # 当前出战的宝可梦
        self.pokemons: list[Pokemon] = pokemons  # 拥有的宝可梦

    def onRoundStart(self):
        """
        回合开始
        """
        self.onFightPokemon.onRoundBegin()

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
