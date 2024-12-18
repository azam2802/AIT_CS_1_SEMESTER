from csv import reader

my_name = "Azam Umarov"

def formExams(file):
    with open(file, "r") as fid:
        freader = reader(fid)
        listReader = [i for i in list(freader)]
        nameIndex = 0
        midtermIndex = 0
        idIndex = 0
        for i in listReader:
            for j,v in enumerate(listReader[:1][0]):
                if v == "names":
                    nameIndex = j
            for j,v in enumerate(listReader[-3:][0]):
                if v == "midterm":
                    midtermIndex = j
            for j,v in enumerate(listReader[:1][0]):
                if v == "id":
                    idIndex = j
        exams = {
            i[nameIndex]: {
                "grades": [v for i, v in enumerate(i[2::]) if i != midtermIndex and i != idIndex],
                "midterm": i[midtermIndex],
            }
            for i in listReader if i[nameIndex] != "name" and i[nameIndex] != "" 
        }
        for i in exams:
            for j, v in enumerate(exams[i]["grades"]):
                try:
                    exams[i]["grades"][j] = int(v)
                except ValueError:
                    exams[i]["grades"][j] = 0
        for i in exams:
            exams[i]["grades"].sort(reverse=True)
            exams[i]["grades"] = exams[i]["grades"][:7]
            try:
                exams[i]["midterm"] = int(exams[i]["midterm"])
            except ValueError:
                exams[i]["midterm"] = 0
    return exams

def getAvg():
    for i,v in formExams("exam_final.csv").items():
        avg = round((sum(v["grades"])/7)*0.7)+(v["midterm"]*0.075)
        yield i, avg

for i in getAvg():
    print(i)