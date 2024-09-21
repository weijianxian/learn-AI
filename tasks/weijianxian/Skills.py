from Basic import Pokemon, Skill


class Thunderbolt(Skill):
    name = "十万伏特"

    def ues(self, target: Pokemon):
        print(f"{self.name} 使用了雷电术")
        target.hp -= 10
