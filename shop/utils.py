from settings import products, prices, quantities, karizdar
# Получить цену определенного товара


def getPrice(products, prices, cart):
    for index, item in enumerate(products):
        if item == cart:
            return prices[index]

# Получить полную сумму корзины


def getTotal(quantity, cart):
    total = 0
    for items, pics in zip(cart, quantity):
        total += getPrice(products, prices, items) * pics
        if items in products:
            index = products.index(items)
            quantities[index] -= pics
    return total

# Добавить запись долга


def kariz(name, debt):
    karizdar.append([name, debt])
    print(f"\nДолг добавлен: {name, debt}\n")

# Получить чек


def getCheck(quantity, cart):
    x = 0
    text = '\n'
    total = getTotal(quantity, cart)
    for items, pics in zip(cart, quantity):
        x = getPrice(products, prices, items) * pics
        text += f'{items} x {pics} -> {x}\n'
    text += "-"*20
    return text + f'\nTotal: {total}\n'

# Спросить у покупателя берет ли он в долг


def checkDebt(customer_all_quantities, customer_all_cart):
    isDebt = input("Вы берете продукты в долг? (yes/no): ")

    if isDebt == "yes":
        name = input("Ваше имя: ")
        isFullDebt = input("Долг равен сумме всей корзины? (yes/no): ")
        if isFullDebt == "no":
            debtSum = int(input("Впишите сумму долга: "))
            kariz(name, debtSum)
        elif isFullDebt == "yes":
            total = getTotal(customer_all_quantities, customer_all_cart)
            kariz(name, total)