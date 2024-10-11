users = {}
events = {}
history = { }

def addUser(nick, name, phone):
    if nick in users:
        return "This user has already been registred"
    else:
        users[name] = {"nick": nick, "name": name, "phone": phone}
        return "User has been registred successfully"
    
def addEvent(sender,reciever,message):
    if sender not in users:
        return f"{sender} is not registred" 
    if reciever not in users:
        return f"{reciever} is not registred" 
    events[len(events)] = {"sender": sender, "reciever":reciever, "message": message}