from django.conf import settings
from pongchilling.models import User

def searchSave(TargetUsername):
    user = User.objects.filter(username = TargetUsername)
    if user:
        return str(user[0]).split(",")[1]
    else:
        return None
    
def getNbUser():
    user = User.objects.all()
    id= 0
    for i in user:
        id+=1
    return id

def clearDB():
    user = User.objects.all()
    for i in user:
        i.delete()

def createUser(NewUsername,NewMdp):
    newUser = User(username=NewUsername,mdp = NewMdp)
    newUser.save()

def getUser(Username):
    user = User.objects.get(username = Username)
    return user

def findUserId(id):
    user = User.objects.get(id=id)
    return user

def removeUser(id):
    user = User.objects.get(id=id)
    user.delete()

def saveLevel(request,levelid):
    TargetUsername= request.session.get("userName")
    user = User.objects.filter(username=TargetUsername)[0]
    user.level = levelid
    user.save()

def deleteByUsername(Username):
    user = User.objects.get(username=Username)
    user.delete()
    print("deleted a user!")

def checkPass(Username,password):
    user = User.objects.filter(username=Username)
    print('input pass word '+password,str(user[0]).split(",")[1])
    if password == str(user[0]).split(",")[1] :

        return True
    else:

        return False
def saveScore(request,score):
    TargetUsername= request.session.get("userName")
    user = User.objects.filter(username=TargetUsername)[0]
    user.currentscore = score

    if user.topscore < score:
        user.topscore = score

    user.save()
