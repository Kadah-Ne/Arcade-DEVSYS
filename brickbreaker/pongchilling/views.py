from django.shortcuts import render
from . import DBFunctions
# Create your views here.
def Login(request):
    return render(request, 'Login.html')

def Index(request):
    if request.method == "POST" and request.POST.dict() !={} and "userName" in request.POST and "password" in request.POST:
        userName = request.POST.dict()["userName"]
        password = request.POST.dict()["password"]
        request.session["username"] = userName
        request.session["mdp"] = password
        foundLevel = DBFunctions.searchSave(userName)
        print("Found Level",foundLevel)
        if foundLevel !=None:
            return render(request,'index.html')
            
        else:
            # DBFunctions.createUser(userName,password)
            return render(request, 'Login.html',{'isNew':True})
    elif request.session["username"] and request.session["mdp"]:
        if "oui" in request.POST :
            DBFunctions.createUser(request.session["username"],request.session["mdp"])
            return render(request,'index.html')
        else : 
          return render(request, 'Login.html',{'isNew':False})
    else :
        return render(request, 'Login.html')