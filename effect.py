# an effect applied by an equippable
class Effect:
    def __init__(self, stat="STR", direction="+/-", amount=0, pointsOrPercent="Pt/%"):
        self.stat = stat
        self.direction = direction
        self.amount = amount
        self.pointsOrPercent = pointsOrPercent

    def __str__(self):
        return self.stat + self.direction + str(self.amount) + " " + self.pointsOrPercent

    def get_amount(self):
        if self.direction == "+":
            return self.amount
        if self.direction == "-":
            return self.amount * -1

    def get_pointsOrPercent(self):
        return self.pointsOrPercent

