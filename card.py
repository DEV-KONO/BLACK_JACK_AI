class card:
    def __init__(self, symbol: str, color: str, value: str):
        self.symbol = symbol
        self.color = color
        self.value = value
        self.visible = True
        pass 

    def __str__(self):
        return f"{self.color} {self.value} of {self.symbol}"

    def flip(self):
        self.visible = not self.visible
