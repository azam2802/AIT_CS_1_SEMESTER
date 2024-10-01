items = {"cola": 50, "mars": 30, "sprite": 20, "shoro": 85}
names = {}


def add_loan(name, item):
    if name not in names:
        names[name] = {"items": []}
        names[name]["sum"] = 0
    for i in items:
        if item == i:
            names[name]["items"].append(item)
            names[name]["sum"] += items.get(item)
    return names
print(add_loan("Azam", "sprite"))
print(add_loan("Azam", "sprite"))
print(add_loan("Emil", "sprite"))


def total_loan(name):
    if name not in names:
        return "Такого нет"
    return names[name]["sum"]

print(total_loan("Atai"))


def get_all_loan_items(name):
    if name not in names:
        return "Такого нет"
    return names[name]["items"]

print(get_all_loan_items("Azam"))
