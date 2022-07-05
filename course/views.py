from django.shortcuts import render

# Create your views here.
def listcourse(req):
    return render(req,'course/List.html')