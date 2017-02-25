class Stock:
    def __init__(self, code, name, comment = ''):
        self.code = code
        self.name = name
        self.comment = comment


class StockRawPrice:
    def __init__(self, code, price, timestamp):
        self.code = code
        self.price = price
        self.timestamp = timestamp