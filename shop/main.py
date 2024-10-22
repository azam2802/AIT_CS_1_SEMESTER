from services import clientService, wholesale, getProductsLeft, getLessProducts
from utils import kariz
from settings import karizdar
# Главная функция

def main():
    while True:
        options = ["1 - Обслуживание покупателя", "2 - Пополнить склад", "3 - Отстатки товаров на складе",
                   "4 - Остатки товаров по количеству", "5 - Записать долг", "6 - Посмотреть должников", "0 - Отмена"]
        for i in options:
            print(i)
        choose = int(input("Выберите опцию: "))
        if choose == 0:
            print("Выход...")
            exit()
        elif choose == 1:
            clientService()
        elif choose == 2:
            print(wholesale())
        elif choose == 3:
            print(f'\nОстатки товаров: {getProductsLeft()}\n')
        elif choose == 4:
            limit = int(input("Введите минимальный порог: "))
            print(f"\nТовары которых осталось меньше {limit}шт: {getLessProducts(limit)}\n")
        elif choose == 5:
            name = input("Имя должника: ")
            debt = int(input("Сумма долга: "))
            kariz(name, debt)
        elif choose == 6:
            print(f'\nДолжники: {karizdar}\n')

# Вызов главной функции при запуске программы
if "__main__" == __name__:
    main()
