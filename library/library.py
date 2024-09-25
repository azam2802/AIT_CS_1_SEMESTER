books = [
    ("Айтматов", ["Первый учитель", "Белый пароход", "Заман"]),
    ("Роулинг", ["Гарри Поттер", "Шелкопряд"]),
]

books_amount = [[10, 15, 8], [4, 10]]

students = [
    ("Аман", ["Гарри Поттер", "Белый пароход"], ["Заман"]),
    ("Азам", ["Гарри Поттер"], ["Жамиля", "Заман"]),
]


def changeBookAmount(operation, book):
    if operation == "-":
        for index, i in enumerate(books):
            if book in i[1]:
                book_index = i[1].index(book)
                books_amount[index][book_index] -= 1
    elif operation == "+":
        for index, i in enumerate(books):
            if book in i[1]:
                book_index = i[1].index(book)
                books_amount[index][book_index] += 1
    return f"Остаток книг: {list(zip(books, books_amount))}"


def borrowBook(student, book):
    library_books = []
    for _, i in books:
        for j in i:
            library_books.append(j)
    print(library_books)
    for a, b, c in students:
        if a == student:
            if book in library_books:
                if book not in c:
                    b.append(book)
                    print(changeBookAmount("-", book))
                else:
                    return "Вы уже брали такую книгу"
            else:
                return "Такой книги нет в библиотеке"
        else:
            students.append((student, list(book), []))
            print(changeBookAmount("-", book))
            return "Вы успешно арендовали книгу из библиотеки."


def returnBook(student, book):
    for a, b, c in students:
        if a == student:
            if book in b:
                b.remove(book)
                c.append(book)
                print(changeBookAmount("+", book))
                print(books_amount)
                return f"Книга '{book}' возвращена."
            else:
                continue
        else:
            continue


def check_books_amount(student):
    for a, b, _ in students:
        if a == student:
            return len(b)


def check_borrowed_books(student):
    for a, b, _ in students:
        if a == student:
            return b


def who_isReading(book):
    reading_students = []
    for i in students:
        if book in i[1]:
            reading_students.append(i[0])
    return reading_students


def check_booksDone(student):
    count = 0
    for a, _, c in students:
        if a == student:
            count += len(c)
    return count


def count_studentsDoneBook(book):
    count = 0
    for _, _, c in students:
        if book in c:
            count += 1
    return count


def author_books_count(author):
    count = 0
    for index, val in enumerate(books):
        if val[0] == author:
            count += sum(books_amount[index])
    return count


def main():
    options = [
        "1 - Сколько книг у студента",
        "2 - Какие книги у студента",
        "3 - Кто читает выбранную книгу",
        "4 - Сколько книг прочитал студент",
        "5 - Сколько студентов прочитали выбранную книгу",
        "6 - Сколько книг у автора в библиотеке",
        "7 - Взять книгу",
        "8 - Вернуть книгу",
        "9 - Выход",
    ]
    for i in options:
        print(i)
    option = int(input("Выберите опцию: "))
    if option == 1:
        print(check_books_amount(input("Имя студента: ")))
    elif option == 2:
        print(check_borrowed_books(input("Имя студента: ")))
    elif option == 3:
        print(who_isReading(input("Название книги: ")))
    elif option == 4:
        print(check_booksDone(input("Имя студента: ")))
    elif option == 5:
        print(count_studentsDoneBook(input("Название книги: ")))
    elif option == 6:
        print(author_books_count(input("Имя автора: ")))
    elif option == 7:
        print(borrowBook(input("Имя студента: "), input("Название книги: ")))
    elif option == 8:
        print(returnBook(input("Имя студента: "), input("Название книги: ")))
    elif option == 9:
        exit()


if "__main__" == __name__:
    main()
