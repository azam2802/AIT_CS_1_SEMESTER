names = ["Azam", "Emil", "Aktan", "Atai"]
amounts = [500, 200, 400, 8000]
history = []


def cancel_transaction():
    if len(transactions) > 0:
        for i in transactions:
            for index, name in enumerate(names):
                if i[1].capitalize() == name:
                    amounts[index] -= int(i[2])
                elif i[0].capitalize() == name:
                    amounts[index] += int(i[2])
            getDetails(f"{i[1].capitalize()} -> {i[0].capitalize()}, {i[2]}som.")
        print(f"Транзакция отменена {list(zip(names, amounts))}\n")
    else: 
        print("\nТранзакции не найдены.\n")


def getDetails(details):
    global details_text
    details_text = "\n"
    details_text += details
    return(details_text)


def validate():
    for i in transactions:
        if i[0].capitalize() not in names or i[1].capitalize() not in names:
            print("Ошибка, проверьте введенные данные")
            exit()
        for index, name in enumerate(names):
            if i[0].capitalize() == name:
                if amounts[index] < int(i[2]):
                    print(f"У {i[0].capitalize()} не достаточно средств для перевода.")
                    exit()


def transfer():
    transfers_count = int(input("Количество транзакций: "))
    global transactions
    transactions = [
        tuple(
            input("Ввдите отправителя, получателя и сумму через запятую: ").split(",")
        )
        for i in range(transfers_count)
    ]

    validate()
    for i in transactions:
        for index, name in enumerate(names):
            if i[1].capitalize() == name:
                amounts[index] += int(i[2])
                history.append(f"{i[0].capitalize()} -> {i[1].capitalize()}, {i[2]}som.")
                print(getDetails(f"{i[0].capitalize()} -> {i[1].capitalize()}, {i[2]}som."))
            elif i[0].capitalize() == name:
                amounts[index] -= int(i[2])
    print(list(zip(names, amounts)))
    return transactions


def main():
    while True:
        option = int(
            input(
                "1 - Перевод\n2 - Отмена последней транзакции\n3 - Просмотр истории\nВыберите дейстивие: "
            )
        )
        if option == 1:
            transfer()
        elif option == 2:
            cancel_transaction()
        elif option == 3:
            print("\nПоследняя транзакция:\n")
            for i in history:
                print(i)


if "__main__" == __name__:
    main()