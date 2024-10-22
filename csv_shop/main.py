import csv

with open("shop.csv", "r") as fid:
    fidRead = csv.reader(fid)
    next(fidRead)
    data = [i for i in fidRead]


def addNew(date, name, tovar, tsena):
    with open("shop.csv", mode="a", newline="") as fid:
        fidWrite = csv.writer(fid)
        fidWrite.writerow([date, name, tovar, tsena])


addNew("2024-12-05", "Emil", "apple", "100")


def totalIncome():
    total = 0
    for i in data:
        total += float(i[3])
    return total


print(totalIncome())


def biggestCartClient():
    max_cart = sorted(data, key=lambda x: float(x[3]), reverse=True)[0]
    return f"{max_cart[1]}, {max_cart[3]}"


print(biggestCartClient())


def mostExpensiveSoldProduct():
    max_price = sorted(data, key=lambda x: float(x[3]), reverse=True)[0]
    counter = 0
    for i in data:
        if max_price[3] in i:
            counter += 1
    return max_price[2], counter


print(mostExpensiveSoldProduct())


def avgOfSales():
    summ = 0
    counter = 0
    for i in data:
        summ += float(i[3])
        counter += 1
    return summ / counter


print(avgOfSales())


def mostIncomeDay():
    d = {}
    for i in data:
        if i[0] not in d:
            d[i[0]] = float(i[3])
        else:
            d[i[0]] += float(i[3])
    return max(d, key=d.get)


print(mostIncomeDay())


def uniqProductsBought():
    d = {}
    for i in data:
        if i[1] not in d:
            d[i[1]] = [i[2]]
        else:
            if i[2] not in d[i[1]]:
                d[i[1]].append(i[2])
    for i in d:
        d[i] = len(d[i])
    return d


print(uniqProductsBought())
