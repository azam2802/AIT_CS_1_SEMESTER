tickets = [False for i in range(1, 101)]
reserves = {}


def sell_ticket(name):
    if name not in reserves:
        reserves[name] = {"tickets": []}
    if len(reserves[name]["tickets"]) < 5:
        if tickets.count(False) > 0:
            for i, v in enumerate(tickets):
                if not v:
                    reserves[name]["tickets"].append(i + 1)
                    tickets[i] = True
                    return f"Thank you {name}! Your ticket number: {i+1}"
    else:
        return "You can't buy more than 5 tickets!"


def show_tickets_left():
    return f"\n{tickets.count(False)} tickets left\n"


def show_tickets_bought():
    text = "\n"
    total_sold = 0
    for i in reserves:
        count = len(reserves[i]["tickets"])
        text += f'{i}: {reserves[i]["tickets"]}, TOTAL: {count}\n'
        total_sold += count
    text += f'Total sold: {total_sold} tickets\n'
    return text


print(sell_ticket("Azam"))
print(sell_ticket("Azam"))
print(sell_ticket("Azam"))
print(sell_ticket("Azam"))
print(sell_ticket("Azam"))
print(sell_ticket("Emil"))
print(sell_ticket("Emil"))
print(show_tickets_left())
print(show_tickets_bought())
