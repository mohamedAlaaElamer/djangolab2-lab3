from django.shortcuts import render
from django.http import HttpResponseRedirect
from course.models import *
# Create your views here.
def listuser(req):
    users=MyUser.objects.all()
    context={}
    context['users']=users
    return render(req,'myuser/list.html',context)
def Update(req,id):
    if(req.session.get('username') is not None):
        context={}
        if(req.method=='GET'):
            context['user']=MyUser.objects.get(id=id)
            return render(req, 'myuser/update.html', context)
        else:
            MyUser.objects.filter(id=id).update(username=req.POST['username'],email=req.POST['username'])
            return HttpResponseRedirect('/User/')#render(req, 'myuser/list.html', context)
    else:
        return HttpResponseRedirect('/')
def Delete(req,id):
    if(req.session.get('username') is not None):
        x=MyUser.objects.filter(id=id).delete()
        return HttpResponseRedirect('/User/')
    else:
        return HttpResponseRedirect('/')