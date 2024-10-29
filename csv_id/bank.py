from collections import defaultdict
from csv import reader
from datetime import datetime
from time import time


with open("mbank_short.csv", "r") as short:
    freader = reader(short)
    next(freader)
    fid_short = {}
    for i in freader:
        if len(i) > 0:
            if i[0] not in fid_short:
                fid_short[i[0]] = []
            fid_short[i[0]].append([i[1], i[2], i[3], i[4]])
    fid_short = dict(sorted(fid_short.items()))

with open("users.csv", "r") as users:
    freader = reader(users)
    fid_user = {str(i[0]): i[1] for i in freader if len(i) > 0}


with open("currencies.csv", "r") as currency:
    freader = reader(currency)
    fid_currency = {str(i[0]): i[1] for i in freader if len(i) > 0}

currencies = {
    "0": 1,
    "1": 85.5,
    "2": 0.88,
    "3": 0.18,
    "4": 92.37,
}


def getName(id):
    return fid_user.get(str(id), "")


def getCurrency(id):
    return fid_currency.get(str(id), "")


def getUsersInfo():
    for i in fid_short:
        for j in fid_short[i]:
            yield f"{datetime.fromtimestamp(int(i))}: {getName(j[0])} -> {getName(j[1])} => {int(j[2])} {getCurrency(j[3])}"


def getUsersTransfers(fromUser, toUser):
    transfers = {}
    for i in fid_short:
        for j in fid_short[i]:
            FromName = getName(j[0])
            ToName = getName(j[1])
            currency = getCurrency(j[3])
            if (
                FromName.upper() == fromUser.upper()
                and ToName.upper() == toUser.upper()
            ):
                if currency not in transfers:
                    transfers.update({currency: float(j[2])})
                else:
                    transfers[currency] += float(j[2])
    if not transfers:
        return "\nТрансферы не найдены"
    else:
        return f"\n{fromUser.upper()} -> {toUser.upper()} => {transfers}"


def whoSendCurrency(currency):
    listOfUsers = []
    for i in fid_short:
        for j in fid_short[i]:
            name = getName(j[0])
            if getCurrency(j[3]).upper() == currency.upper():
                if name not in listOfUsers:
                    listOfUsers.append(name)
                    yield f"{name} отправлял(а) {currency}"


def whoSentTo(toUser):
    transfers = {}
    for i in fid_short:
        for j in fid_short[i]:
            name = getName(j[0])
            currency = getCurrency(j[3])
            if getName(j[1]).upper() == toUser.upper():
                if name not in transfers:
                    transfers[name] = {}
                if currency not in transfers[name]:
                    transfers[name][currency] = float(j[2])
                else:
                    transfers[name][currency] += float(j[2])
    if not len(transfers):
        return "Трансферы не найдены"
    else:
        return f"\nПользователи которые переводили {toUser.upper()}: {transfers}"


def getFeeIncome():
    income = 0
    for i in fid_short:
        for v in fid_short[i]:
            for j in currencies:
                if j == v[3]:
                    income += float(v[2]) * currencies[j]
    return f"\nИтого заработано: {(income):.3f} сом"


def top5Transfers():
    d = defaultdict(lambda: [0,0])
    for i in fid_short:
        for j in fid_short[i]:
            nameSender = getName(j[0])
            nameReciever = getName(j[1])
            amount = float(j[2]) * currencies[j[3]]
            d[nameSender][0] += amount
            d[nameReciever][1] += amount
    d = sorted(d.items(), key=lambda x: x[1][0], reverse=True)[:5]
    d_send = sorted(d, key=lambda x: x[1][1], reverse=True)[:5]
    text = "\nTop Senders:\n".join(f"{name}: {amount[0]}" for name, amounts in d)
    for i in d:
    text += "\nTop Recievers\n"
    for i in d_send:
        text += f"{i[0]}: {i[1][1]}\n"
    return text

def transactionsPerDay():
    for i in fid_short:
        summ = 0
        for j in fid_short[i]:
            summ += float(j[2]) * currencies[j[3]]
        yield f"{datetime.fromtimestamp(int(i))}: {len(fid_short[i])} транзакций, {summ} сом"


def avgUsersTransaction():
    users = {}
    for i in fid_short:
        for j in fid_short[i]:
            name1 = getName(j[0])
            name2 = getName(j[1])
            if name1 not in users:
                users[name1] = {"amount": 0, "count": 0}
            if name2 not in users:
                users[name2] = {"amount": 0, "count": 0}
            users[name1]["amount"] += float(j[2]) * currencies[j[3]]
            users[name1]["count"] += 1
    for i in users:
        try:
            users[i] = round(users[i].get("amount", 0) / users[i].get("count"), 3)
        except ZeroDivisionError:
            users[i] = "No transactions"
    return "\n".join(f"{i} => {users.get(i)} сом." for i in users)


def onlyOneCurrencyUser():
    users = {}
    for i in fid_short:
        for j in fid_short[i]:
            name = getName(j[0])
            currency = getCurrency(j[3])
            if name not in users:
                users[name] = {
                    "amount": 0,
                    "currencies": [],
                }
            users[name]["amount"] += float(j[2])
            users[name]["currencies"].append(currency)
    return "\n".join(
        f"{i}: {users[i]["amount"]} {users[i]["currencies"][0]}"
        for i in users
        if len(users[i]["currencies"]) == 1
    )


def mostActiveUser(sortParam="count"):
    users = {}
    for i in fid_short:
        for j in fid_short[i]:
            name = getName(j[0])
            if name not in users:
                users[name] = {"count": 0, "amount": 0}
            users[name]["count"] += 1
            users[name]["amount"] += float(j[2]) * currencies[j[3]]
    users = dict(sorted(users.items(), key=lambda x: x[1][sortParam], reverse=True)[:1])
    return "".join(
        f"{i}: {users[i]["count"]} операций на {round(users[i]["amount"], 3)} сом."
        for i in users
    )


def mostActiveDay():
    summ = 0
    days = {}
    for i in fid_short:
        date = datetime.fromtimestamp(int(i)).strftime("%Y-%m-%d")
        if date not in days:
            days[date] = []
        for j in fid_short[i]:
            days[datetime.fromtimestamp(int(i)).strftime("%Y-%m-%d")].append(j)
    days = dict(sorted(days.items(), key=lambda x: len(x[1])))
    for i in days:
        for j in days[i]:
            summ += round(float(j[2]) * currencies[j[3]], 3)
    return "".join(f"{i}: {len(days[i])} транзакций на сумму {summ}")


def main():
    options = [
        "\n1 - Получить информацию о переводах",
        "2 - Получить информацию о переводах пользователя к пользователю",
        "3 - Получить информацию о переводах в конкретной валюте",
        "4 - Получить информацию о переводах определенному пользователю",
        "5 - Получить информацию об итоговом заработке на комисии",
        "6 - Топ 5 отправителей и получателей",
        "7 - Получить информацию о транзакциях за каждый день",
        "8 - Получить информацию о среднем объеме транзакций пользователя",
        "9 - Получить информацию о пользователяй которые использовали только одну валюту",
        "10 - Получить информацию о самом активном пользователе по кол-ву транзакций",
        "11 - Получить информацию о самом активном пользователе по сумме транзакций",
        "12 - Получить информацию о самом активном дне по кол-ву транзакций",
        "0 - Выход",
    ]
    for i in options:
        print(i)
    i = int(input("\nВыберите действие: "))
    while i != 0:
        if i == 1:
            for i in getUsersInfo():
                print(i)
        elif i == 2:
            print(getUsersTransfers(input("\nОт: "), input("\nКому: ")))
        elif i == 3:
            currencies = [0, 1, 2, 3, 4]
            print("\n")
            for i in currencies:
                print(f"{i+1} - {getCurrency(i)}")
            choise = int(input("\nВыберите валюту: "))
            currency = getCurrency(choise - 1)
            for i in whoSendCurrency(currency):
                print(i)
        elif i == 4:
            print(whoSentTo(input("Введите имя пользователя: ")))
        elif i == 5:
            print(getFeeIncome())
        elif i == 6:
            st = time()
            print(top5Transfers())
            en = time()
            print(en - st)
        elif i == 7:
            for i in transactionsPerDay():
                print(i)
        elif i == 8:
            print(avgUsersTransaction())
        elif i == 9:
            print(onlyOneCurrencyUser())
        elif i == 10:
            start = time()
            print(mostActiveUser())
            end = time()
            print(end - start)
        elif i == 11:
            print(mostActiveUser("amount"))
        elif i == 12:
            print(mostActiveDay())
        for i in options:
            print(i)
        i = int(input("\nВыберите действие: "))


if "__main__" == __name__:
    main()
