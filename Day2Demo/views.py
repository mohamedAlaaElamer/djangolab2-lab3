from django.shortcuts import render
from course.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as  authlogin,logout as authlogout
def Homeview(req):
    if (req.session.get('username') is None):
        return render(req,'index.html',{'viewname':'Home'})
    else:
        return render(req, 'login.html')
def Register(req):
    if(req.method=='GET'):
        return render(req,'register.html')
    else:
        #get data
        print(req.POST)
        #insert db
        '''
        u=MyUser(username=req.POST['username'])
        u.email=req.POST['email']
        u.password=req.POST['password']
        u.save()
        '''
        #ctreat user in myuser model
        u= MyUser.objects.create(username=req.POST['username'],email=req.POST['email'],password=req.POST['password'])
        User.objects.create_user(username=req.POST['username'],email=req.POST['email'],password=req.POST['password'],is_superuser=True,is_staff=True)
        #redirect to login
        return render(req, 'login.html')

def Login(req):
    #req.session.clear()
    if(req.session.get('username') is None):
        if(req.method=='GET'):
            return render(req, 'login.html')
        else:
            #check user cred in myuser
            myuserobject= MyUser.objects.filter(username=req.POST['username'],password=req.POST['password'])
            # check user cred in authuser
            authuserobject=authenticate(username=req.POST['username'],password=req.POST['password'])
            if(len(myuserobject)>0 and authuserobject is not None):
                req.session['username']=myuserobject[0].username
                authlogin(req,authuserobject)
                return render(req, 'index.html')
            else:
                print('errrrro')
                context={}
                context['error']='invalid cred.'

                return render(req, 'login.html',context)
    else:
        return render(req,'index.html')

def logout(req):
    if (req.session.get('username') is None and req.user.is_authenticated()):
        req.session.clear()
        authlogout(req,req.user)
    return render(req,'index.html')