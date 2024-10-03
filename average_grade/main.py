names = {}

def getText(name, label, text):
    return f"\n\t***{name.capitalize()}'s {label}***\n"+text

def addGrade(name, grade, quiz):
    if name not in names:
        names[name] = {"quizes": [], "grades": []}
    for i in names:
        if i == name:
            names[i]["quizes"].append(quiz)
            names[i]["grades"].append(grade)

addGrade("emil", 100, "midterm")
addGrade("emil", 70, "midterm2")
addGrade("emil", 67, "midterm3")
addGrade("emil", 23, "midterm3")
addGrade("azam", 100, "midterm3")
addGrade("azam", 45, "midterm3")
addGrade("azam", 75, "midterm3")
addGrade("azam", 60, "midterm3")

def getGrades(name):
    text = ""
    if name in names:
        for i, v in enumerate(names[name]["quizes"]):
            text += f'{v}: {names[name]["grades"][i]}\n'
    else:
        return "Student not found"
    return getText(name, "grades", text)

print(getGrades("emil"))

def getAverage(name):
    text = ""
    grades = names[name]["grades"]
    avg = 0
    if name in names:
        avg += sum(grades)/len(grades)
        text += f'Average: {avg}\n'   
    else:
        return 'Students not found'
    return getText(name, "average", text), avg

print(getAverage('emil')[0])    

def getAllAverage():
    text = ""
    for i in names:
        text += f'{i}: {getAverage(i)[1]}\n'
    return getText("Everyone", "averages", text)

print(getAllAverage())

def getHighestScore():
    for i in names:
        