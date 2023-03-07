from django.conf import settings
from pongchilling.models import User

def searchSave(TargetUsername):
    user = User.objects.filter(username = TargetUsername)
    if user:
        return str(user[0].split(",")[1])
    else:
        return None
def createUser(NewUsername,NewMdp):
    newUser = User(username=NewUsername,mdp = NewMdp)
    newUser.save()

def saveLevel(request,levelid):
    TargetUsername= request.session.get("userName")
    user = User.objects.filter(username=TargetUsername)[0]
    user.level = levelid
    user.save()

def saveScore(request,score):
    TargetUsername= request.session.get("userName")
    user = User.objects.filter(username=TargetUsername)[0]
    user.currentscore = score

    if user.topscore < score:
        user.topscore = score

    user.save()
