class Dollar:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int):
        # 重複を除去: 10 は 5 * 2 であり、それは amount * multiplier である
        self.amount *= multiplier
