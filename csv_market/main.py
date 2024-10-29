from csv import reader

with open("distributor.csv", "r") as fid:
    freader = reader(fid)
    next(freader)
    distributors = {i[0]: {"name": i[1], "phone": i[2]} for i in freader}

with open("products.csv", "r") as fid:
    freader = reader(fid)
    next(freader)
    products = {i[0]: {"name": i[1], "weight": i[2]} for i in freader}

with open("purchase.csv", "r") as fid:
    next(fid)
    freader = reader(fid)
    purchases = [i for i in freader]

with open("sales.csv", "r") as fid:
    next(fid)
    freader = reader(fid)
    sales = [i for i in freader]


def productsQuantity():
    for i in products:
        count = 0
        for j in purchases:
            if i == j[2]:
                count += 1
        yield f"{products[i]["name"]} был куплен {count} раз"


for i in productsQuantity():
    print(i)


def getTotalIncome():
    for i in products:
        income = 0
        for j in sales:
            if i == j[2]:
                income += float(j[5])
        yield f"{products[i]["name"]} был продан на сумму {round(income, 3)} сом"


for i in getTotalIncome():
    print(i)


