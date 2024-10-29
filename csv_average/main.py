from csv import reader

with open("exam2.csv", "r") as fid:
    freader = reader(fid)
    next(freader)
    freader = [i for i in list(freader)]
    for i in freader:
        try:
            int(i[14])
            i[13], i[14] = i[14], ""
        except:
            pass      
    exams = {
        i[1]: {
            "grades": [v for i, v in enumerate(i[2::]) if i != 10],
            "midterm": i[12],
        }
        for i in freader
    }

    for i in exams:
        for j, v in enumerate(exams[i]["grades"]):
            try:
                exams[i]["grades"][j] = int(v)
            except ValueError:
                exams[i]["grades"][j] = 0
    for i in exams:
        exams[i]["grades"].sort(reverse=True)
        exams[i]["grades"] = exams[i]["grades"][:6]
        try:
            exams[i]["midterm"] = int(exams[i]["midterm"])
        except:
            exams[i]["midterm"] = 0
    exams.pop("")

def getAvg():
    for i,v in exams.items():
        avg = ((sum(v["grades"])/6)*0.7)+(v["midterm"]*0.075)
        yield i, avg

for i in getAvg():
    print(i)

