movie_titles = ["Marvel", "Spider-Man", "Oppenheimer", "Barby"]
viewers_names = [[] for i in movie_titles]
seat_numbers = [[] for i in movie_titles]


def reserv_seat(name, movie, seat):
    for index, value in enumerate(movie_titles):
        if movie == value:
            viewers_names[index].append(name)
            seat_numbers[index].append(seat)
            print(f"\nМесто {seat} на фильм {movie} зарезервировано для {name}\n")
            return print_ticket(movie, name, seat)


def delete_reservation(param):
    for index, value in enumerate(viewers_names):
        if param in value:
            seat_index = value.index(param)
            seat = seat_numbers[index][seat_index]
            value.remove(param)
            seat_numbers[index].pop(seat_index)
            return f"Бронь места {seat} для {param} удалена успешно!"
    else:
        for index, value in enumerate(seat_numbers):
            if int(param) in value:
                viewer_index = value.index(int(param))
                viewer = viewers_names[index][viewer_index]
                value.remove(int(param))
                viewers_names[index].pop(viewer_index)
                return f"Бронь места {param} для {viewer} удалена успешно!"
            else:
                continue


def print_ticket(movie, name, seat):
    text = f'{'='*30}\nФильм: {movie}\nИмя зрителя: {name}\nМесто: {seat}\n{'='*30}\n'
    return text


def main():
    options = [
        "1 - Добавить бронь",
        "2 - Удалить бронь",
        "3 - Список фильмов",
        "4 - Посмотреть все брони",
        "5 - Выход",
    ]
    for i in options:
        print(i)
    option = int(input("Выберите опцию: "))
    if option == 1:
        print(
            reserv_seat(
                input("Имя зрителя: ").capitalize(),
                input("Название фильма: ").capitalize(),
                int(input("Место: ")),
            )
        )
    elif option == 2:
        print(delete_reservation(input("Введите имя зрителя или его место: ")))
    elif option == 3:
        print(f"Список всех фильмов: {movie_titles}")
    elif option == 4:
        print(list(zip(movie_titles, viewers_names, seat_numbers)))
    elif option == 5:
        exit()


if "__main__" == __name__:
    while True:
        main()
