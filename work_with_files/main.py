import os 


def find_word(folder, word):
    files = os.listdir(folder)
    for i in files:
        try:
            file = open(i, "r")
        except IsADirectoryError:
            pass
        except PermissionError:
            pass
        lines = file.readlines()
        for j, v in enumerate(lines):
            if word in v:
                print(i, j + 1)


find_word("C:\\AIT\\Python\\work_with_files", "asdadasd")


def count_files(folder):
    return len(os.listdir(folder))


print(count_files("C:\\AIT\\Python\\work_with_files"))

def max_length_word(filename):
    try:
        file = open(filename, "r")
    except IsADirectoryError:
        pass
    except PermissionError:
        pass
    lines = file.readlines()
    words = []
    for i in lines:
        words += i.strip().split()
    for i, v in enumerate(words):
        max_letters = float('-inf')
        if len(v) > max_letters:
            max_letters = len(v)
            max_word_index = i 
    return f"Longest word in {filename}: {words[max_word_index]}" 


print(max_length_word("main.py"))
