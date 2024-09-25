from settings import quantities, products, cart, cart_quantities
from utils import checkDebt, getCheck

# Пополнить склад продуктов


def wholesale():
    max = 100
    for index, ostatok in enumerate(quantities):
        if ostatok < 100:
            quantities[index] = max
    return "Склад пополнен"


# Получение из списка продуктов которых осталось меньше определенного кол-ва


def getLessProducts(limit):
    x = [(product, quantities[index]) for index, product in enumerate(
        products) if quantities[index] < limit]
    return x

# Получить остатки товаров


def getProductsLeft():
    ostatok = list(zip(products, quantities))
    return ostatok


# Обслуживание покупателя


def clientService():
    customers_num = int(input("Сколько покупателей: "))
    for i in range(1, customers_num+1):
        products_num = int(
            input(f"Покупатель {i} сколько продуктов вы хотите купить: "))
        customer_all_cart = [input(f"Покупатель {i} введите продукт {
                                   j}: ") for j in range(1, products_num+1)]
        customer_all_quantities = [int(input(f"Покупатель {i} введите количество продуктa {
                                       j}: ")) for j in range(1, products_num+1)]
        
        checkDebt(customer_all_quantities, customer_all_cart)
        
        cart.append(customer_all_cart)
        cart_quantities.append(customer_all_quantities)
    for cart_i, cart_quantities_i in zip(cart, cart_quantities):
        print(getCheck(cart_quantities_i, cart_i))
