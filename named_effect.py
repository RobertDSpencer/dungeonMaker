# an effect with a name
class NamedEffect:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return self.quality + self.name
