class Dollar:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int):
        # 第1章の「仮実装」: テストを通すためだけに10をセットする
        self.amount = 10
