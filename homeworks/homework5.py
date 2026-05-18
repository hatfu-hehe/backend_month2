
class Streamer:
    def live(self):
        return "Запускаю стрим!"
    def earn(self):
        return "Заработал 500 донатов"

class TikToker:
    def live(self):
        return "Снимаю тикток!"
    def viral(self):
        return "3 миллиона просмотров!"

class Mutant:
    def live(self):
        return "Свечусь в темноте..."
    def superpower(self):
        return "Летаю и стреляю лазерами"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()} + {self.earn()}"

class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()} + {self.viral()}"

class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"{self.live()} + {self.viral()} + {self.earn()}"


for cls in [GlowStreamer, ViralCyborg, DonateMage]:
    obj = cls()
    print(f"{cls.__name__}")
    print(f"MRO: {[c.__name__ for c in cls.__mro__]}")
    print(f"{obj.live()}")
    print(obj.ultimate_content())