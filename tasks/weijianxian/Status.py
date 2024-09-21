from Basic import Pokemon, Status


class PoisonStatus(Status):
    name = "中毒"
    priority = 1
    continue_round = 3

    def on_begin(self, pokemon: Pokemon):
        print(f"{pokemon.name} 中毒了")
        pokemon.hp -= int(pokemon.hp * 0.1)
