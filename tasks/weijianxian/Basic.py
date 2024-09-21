class Player:
    def __init__(
        self,
        name: str,
        pokemons: list["Pokemon"],
    ):
        self.name: str = name  # 玩家名称
        self.onFightPokemon: Pokemon = None  # 当前出战的宝可梦
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

    def switchPokemon(self, pokemon: "Pokemon"):
        """
        切换宝可梦
        """
        if pokemon not in self.pokemons:
            raise ValueError("宝可梦不在列表中")

        self.onFightPokemon = pokemon


class Pokemon:
    """
    基础宝可梦类

    name: 宝可梦名称
    hp: 宝可梦生命值
    type: 宝可梦类型
    attack: 宝可梦攻击力
    defense: 宝可梦防御力
    evasion: 宝可梦闪避率 0-100 之间,
    status: 宝可梦状态
    """

    name: str = ""
    hp: int = 0
    type: "PokemonType" = None
    attack: int = 0
    defense: int = 0
    evasion: int = 0
    status: list["Status"] = []

    def __str__(self):
        return f"{self.name}({self.type.name})"

    def onRoundBegin(self):
        """
        宝可梦战斗回合开始
        """
        pass

    def onRoundEnd(self):
        """
        宝可梦战斗回合结束
        """
        pass


class PokemonType:
    """
    基础宝可梦类型类

    name: 宝可梦类型名称
    strong_against: 强势对手
    weak_against: 弱势对手
    """

    name: str = ""

    strong_against: list["PokemonType"] = []
    weak_against: list["PokemonType"] = []

    def on_begin(self):
        for status in self.status:
            status.on_begin(self)


class Skill:
    name = "BasicSkill"

    def ues(self, target: Pokemon):
        pass


class Status:
    """
    Represents a basic status in the Pokemon game.
    Attributes:
        name (str): 名称
        priority(int): 越大越先执行,0为最后执行,同优先级按照加入顺序
        continue_round (int): 持续回合数,-1为永久,0为即时
    """

    name = "BasicStatus"
    priority = 0
    continue_round = 0

    def on_begin(self, pokemon: Pokemon):
        """
        状态开始时触发
        """
        pass
