flight_numbers = [1254, 5535, 1202, 746]
passenger_names = [[] for i in flight_numbers]
seats = [[] for i in flight_numbers]


def add_passenger(name, seat, flight):
    for index, value in enumerate(flight_numbers):
        if flight == value:
            passenger_names[index].append(name)
            seats[index].append(seat)
            print("Пассажир успешно добавлен!")
            return print_ticket(name, seat, flight)
        else:
            continue

def delete_passenger(param):
    for index, value in enumerate(seats):
        if param in value:
            seat_index = value.index(param)
            value.remove(param)
            passenger = passenger_names[index][seat_index]
            passenger_names[index].pop(seat_index)
            return f"\nПассажир {passenger} успешно удален!\n"

        else:
            for index1, value1 in enumerate(passenger_names):
                if param in value1:
                    name_index = value1.index(param)
                    value1.remove(param)
                    seats[index1].pop(name_index)
                    return f"\nПассажир {param} успешно удален!\n"
                else:
                    continue


def print_ticket(name, seat, flight):
    text = f"{"="*30}\nPassenger's name: {name}\nFlight number: {flight}\nSeat number: {seat}{"\n"+"="*30}"
    return text


def main():
    options = [
        "1 - Добавить пассажира",
        "2 - Удалить пассажира",
        "3 - Список рейсов",
        "4 - Выход",
    ]
    for i in options:
        print(i)
    option = int(input("Выберите опцию: "))
    if option == 1:
        print(
            add_passenger(
                input("Имя пассажира: "),
                input("Номер посадочного места: "),
                int(input("Номер рейса: ")),
            )
        )
    elif option == 2:
        print(
            delete_passenger(input("Введите имя пассажира или его посадочное место: "))
        )
    elif option == 3:
        print(f"Список всех рейсов: {flight_numbers}")
    elif option == 4:
        exit()


if "__main__" == __name__:
    while True:
        main()
