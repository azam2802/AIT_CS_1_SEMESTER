names = {}


def getText(label, text=""):
    return f"\n\t*** {label} ***\n" + text


def getStudents(group):
    return [i for i in names[group]]


def validate(name, quiz, group):
    if group in names:
        if name in names[group]:
            if quiz or quiz in names[group][name]["quizes"]:
                return True, True
            else:
                return getText(f"{name.capitalize()} was absent"), False
        else:
            return getText(
                f"{name.capitalize()} is not in group {group.upper()}"
            ), False
    else:
        return getText(f"Group {group.upper()} not found"), False


def getQuizes(group):
    quizes = []
    for i in getStudents(group):
        for j in names[group][i]["quizes"]:
            if j not in quizes:
                quizes.append(j)
    return quizes


def addGrade(name, grade, quiz, group):
    if group not in names:
        names[group] = {}
    if name not in names[group]:
        names[group][name] = {"quizes": [], "grades": []}
    for i in names:
        if i == group:
            names[group][name]["quizes"].append(quiz)
            names[group][name]["grades"].append(grade)


addGrade("emil", 100, "midterm2", "cs2023")
addGrade("azam", 70, "midterm3", "cs2023")
addGrade("atai", 67, "midterm2", "cs2023")
addGrade("atai", 67, "quiz", "cs2023")
addGrade("emil", 95, "quiz", "cs2023")
addGrade("atai", 70, "quiz", "cs2024")
addGrade("azam", 100, "quiz", "cs2024")
addGrade("azam", 100, "midterm3", "cs2024")
addGrade("azam", 45, "midterm3", "cs2024")
addGrade("azam", 75, "midterm3", "cs2024")
addGrade("azam", 60, "midterm3", "cs2024")


def getGrades(name, group="cs2023"):
    text = ""
    if name in names[group]:
        for i, v in enumerate(names[group][name]["quizes"]):
            text += f'{v}: {names[group][name]["grades"][i]}\n'
    else:
        return "Student not found"
    return getText(f"{name.capitalize()}'s grades", text)


print(getGrades("emil", "cs2023"))


def getAverage(name, group="cs2023", isAll=False):
    text = ""
    avg = 0
    if validate(name, True, group)[1]:
        grades = names[group][name]["grades"]
        avg += sum(grades) / len(grades)
        text += f"Average: {avg}\n"
    else:
        return validate(name, True, group)[0]
    if not isAll:
        print(getText(f"{name.capitalize()}'s average", text))
    return avg


print(getAverage("eml", "cs2023"))


def getAllAverages(group="cs2023"):
    text = ""
    if group in names:
        for i in getStudents(group):
            text += f"{i}: {getAverage(i, group, True)}\n"
    else:
        return getText(f"Group {group.upper()} not found")
    return getText("All averages", text)


print(getAllAverages("cs2023"))


def getStatOfStudents(quiz, group="cs2023"):
    text = ""
    count = 0
    grades_for_quiz = []
    if group in names:
        for i in getStudents(group):
            if quiz in names[group][i]["quizes"]:
                count += 1
                grades_for_quiz.append(
                    names[group][i]["grades"][names[group][i]["quizes"].index(quiz)]
                )
    else:
        return getText(f"Group {group.upper()} not found")
    avg = sum(grades_for_quiz) / len(grades_for_quiz)
    maxGrade = max(grades_for_quiz)
    minGrade = min(grades_for_quiz)
    text += f"Min grade: {minGrade}\nMax grade: {maxGrade}\nStudents quantity: {count}\nAverage for quiz: {avg}\n"
    return (
        getText(f"{quiz.capitalize()} statistics", text),
        count,
        avg,
        maxGrade,
        minGrade,
    )


print(getStatOfStudents("midterm3", "cs2"))


def getAllStats(group):
    for i in getQuizes(group):
        print(getStatOfStudents(i, group)[0])


getAllStats("cs2023")


def getAbsentStudents(students, quiz, group):
    text = ""
    absents_students = [
        i.capitalize() for i in students if quiz not in names[group][i]["quizes"]
    ]
    for i in absents_students:
        text += f"{i}\n"
    return getText(f"Absent students on {quiz}", text)


print(getAbsentStudents([i for i in names["cs2023"]], "midterm3", "cs2023"))


def getMissedQuizes(name, group):
    text = ""
    if validate(name, True, group)[1]:
        for i in getQuizes(group):
            if i not in names[group][name]["quizes"]:
                text += i + "\n"
    else:
        return validate(name, True, group)[0]
    return getText(f"{name.capitalize()} was absent during", text)


print(getMissedQuizes("emil", "cs2023"))


def updateGrade(name, group, quiz, grade):
    if validate(name, quiz, group)[1]:
        quiz_index = names[group][name]["quizes"].index(quiz)
        names[group][name]["grades"][quiz_index] = grade
    else:
        return validate(name, quiz, group)[0]
    return getText(f"{name.capitalize()}'s grade was updated", f"{quiz}: {grade}")


print(updateGrade("emil", "cs2023", "midterm2", 95))


def deleteGrade(name, group, quiz):
    if validate(name, quiz, group)[1]:
        quiz_index = names[group][name]["quizes"].index(quiz)
        names[group][name]["quizes"].pop(quiz_index)
        names[group][name]["grades"].pop(quiz_index)
    else:
        return validate(name, quiz, group)[0]
    return getText(f"{name.capitalize()}'s grade for {quiz} was deleted")


print(deleteGrade("emil", "cs2024", "midterm3"))


def compareStats(group1, group2):
    quizes1 = set()
    quizes2 = set()
    for i in getStudents(group1):
        for j in names[group1][i]["quizes"]:
            quizes1.add(j)
    for i in getStudents(group2):
        for j in names[group2][i]["quizes"]:
            quizes2.add(j)
    quizes3 = quizes1.intersection(quizes2)
    for i in quizes3:
        group1_stats = getStatOfStudents(i, group1)
        group2_stats = getStatOfStudents(i, group2)
        minDiff = group1_stats[4] - group2_stats[4]
        maxDiff = group1_stats[3]-group2_stats[3]
        avgDiff = group1_stats[2]-group2_stats[2]
        countDiff = group1_stats[1]-group2_stats[1]
        text = f"{group1.upper()} and {group2.upper()} min grade difference: {group1_stats[4]}-{group2_stats[4]} = {minDiff}\n"
        text += f"{group1.upper()} and {group2.upper()} max grade difference: {group1_stats[3]}-{group2_stats[3]} = {maxDiff}\n"
        text += f"{group1.upper()} and {group2.upper()} average grade difference: {group1_stats[2]}-{group2_stats[2]} = {avgDiff}\n"
        text += f"{group1.upper()} and {group2.upper()} quantity difference: {group1_stats[1]}-{group2_stats[1]} = {countDiff}\n"
        print(getText(f"{group1.upper()} and {group2.upper()} comparing {i}", text))


compareStats("cs2023", "cs2024")