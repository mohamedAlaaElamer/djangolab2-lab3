from django.shortcuts import render ,HttpResponseRedirect
from .forms import *
from .models import *
from django.views.generic import *



# Create your views here.
def listtrainee(req):
    return render(req,'trainee/list.html')

def traineeinsert(req):
    context={}
    form=InsertTrainee2()
    if(req.method=='GET'):
        context['form']=form
        return render(req,'trainee/traineeinsert.html',context)
    else:
        #get form data & cretae object from trainee
        form=InsertTrainee2(req.POST)
        if(form.is_valid()):
            form.save()
        #redirect to list trainees
        return HttpResponseRedirect('/Trainee')

class traineeupdate(UpdateView):
    model = Trainee
    fields = '__all__'

class deletetrainee(View):
    def get(self,req):
        context={}
        context['subs']=Trainee.objects.all()
        return render(req,'trainee/trainee_delete.html',context)

    def post(self,req):
        Trainee.objects.get(id=req.POST['determine']).delete()
        context = {}
        context['subs'] = Trainee.objects.all()
        return render(req, 'trainee/trainee_delete.html',context)
