class Kofeyna:
    def __init__(self):
        self.personal = None
        self.history = []
        self.sell_prices = {}
        self.purchase_prices = {}
        self.quantities = {}
        self.total = 0
        self.total_income = 0
        self.purchase_history = []

    def getCurrentPersonal(self):
        return self.personal

    def SetCurrentPersonal(self, personal):
       self.personal = personal
       return "Personal changed"

    def getHistory(self):
       return self.history
     
    def sellItems(self, item_name):
        price = self.get(self.prices, 0)
        if self.quantities[item_name] == 0:
            return "item doesn't exist"
        self.quantities[item_name] -= 1
        self.history.append(f'{item_name} -> {price} : {self.personal}')
        self.total += price
        self.total_income += price - self.purchase_prices[item_name]

    def getProfit(self):
        return self.total_income

    def getKassa(self):
        return self.total

    def addProduct(self, purchase_price, product_name, quantity):
        if product_name not in self.quantities:
            self.quantities[product_name] = 0
        if product_name not in self.purchase_prices:
            self.purchase_prices[product_name] = 0
        self.quantities[product_name] += quantity
        self.purchase_prices[product_name] += purchase_price
        self.sell_prices[product_name] += purchase_price * 1.3
        self.purchase_history.append(f'{product_name} -> {purchase_price}, {quantity} : {self.personal}')
        return "Purcahse from diller added"
    
    def getItems(self):
        arr = []
        for i in self.quantities:
            if self.quantities[i] > 0:
                arr.append(f'{i} -> {self.quantities.get(i)}')