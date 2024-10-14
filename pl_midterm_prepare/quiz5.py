schedule = {}


def addTrain(arrival, time):
    if arrival in schedule:
        if time not in schedule[arrival]["time"]:
            schedule[arrival]["time"].append(time)
            return f"Train {arrival} at {time} was added successfully"
        return f"Train {arrival} at {time} has been already added"
    schedule[arrival] = {"time": [time]}
    return f"Train to {arrival} at {time} was added successfully"


print(addTrain("Osh", "15:30"))

print(addTrain("Osh", "11:30"))
print(addTrain("Osh", "13:00"))
print(addTrain("Karakol", "15:30"))
print(addTrain("Karakol", "10:30"))
print(addTrain("Karakol", "8:30"))
print(addTrain("Karakol", "8:00"))


def findByArrival(arrival):
    result = "\n"
    for i in schedule:
        if i.lower() == arrival.lower():
            for j in schedule[i]["time"]:
                result += f"Found train to {arrival.capitalize()} at {j}\n"
    return result if len(result) > 1 else "No trains were found"


print(findByArrival("Karakol"))


def findAllByTime():
    result = "\n"
    for i in schedule:
        minTime = schedule[i]["time"][0]
        for j in schedule[i]["time"]:
            if int(j.split(":")[0]) < int(minTime.split(":")[0]):
                minTime = j
            elif int(j.split(":")[0]) == int(minTime.split(":")[0]):
                if int(j.split(":")[1]) < int(minTime.split(":")[1]):
                    minTime = j
        result += f"Next train to {i} is at {minTime}\n"
    return result

print(findAllByTime())
