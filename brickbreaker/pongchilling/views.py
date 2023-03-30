from django.shortcuts import render
from . import DBFunctions
# Create your views here.
def Login(request):
    return render(request, 'Login.html')

def Index(request):
    if request.method == "GET" and request.GET.dict() !={} and request.GET.dict()["userName"] != "" and request.GET.dict()["password"] != "":
        userName = request.GET.dict()["userName"]
        password = request.GET.dict()["password"]
        request.session["username"] = userName
        foundLevel = DBFunctions.searchSave(userName)
        print(foundLevel)
        if foundLevel !=None:
            return render(request,'index.html')
        else:
            DBFunctions.createUser(userName,password)
            return render(request, 'index.html')
            
    else :
        return render(request, 'Login.html')