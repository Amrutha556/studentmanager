from django.shortcuts import render,redirect
from django.views import View
from .forms import StudentForm,RegForm,LogForm
from .models import Students
from django.contrib.auth import authenticate

# Create your views here.

class LoginView(View):
    def get(self,request):
        form=LogForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        formdata=LogForm(data=request.POST)
        if formdata.is_valid():
            uname=formdata.cleaned_data.get('username')
            pswd=formdata.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                return redirect('landing')
            else:
                return redirect('log')
        return render(request,"login.html",{"form":formdata})

class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request):
        formdata=RegForm(data=request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('log')
        return render(request,"reg.html",{"form":formdata})

class LandingView(View):
    def get(self,request):
        return render(request,"landing.html")
    
class DashboardView(View):
    def get(self,request):
        data=Students.objects.all()
        return render(request,"dash.html",{"data":data})

class AddStudentView(View):
    def get(self,request):
        form=StudentForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        formdata=StudentForm(data=request.POST)
        if formdata.is_valid():
            roll_no=formdata.cleaned_data.get('roll_no')
            name=formdata.cleaned_data.get('name')
            cource=formdata.cleaned_data.get('cource')
            subject=formdata.cleaned_data.get('subject')
            phone_no=formdata.cleaned_data.get('phone_no')
            Students.objects.create(roll_no=roll_no,name=name,cource=cource,subject=subject,phone_no=phone_no)
            return redirect('dash')
        return render(request,"add.html",{"form":formdata})

class DeleteStudentView(View):
    def get(self,request,*args,**Kwargs):
        tid=Kwargs.get('id')
        task=Students.objects.get(id=tid)
        task.delete()
        return redirect('dash')
    
class EditStudentView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        task=Students.objects.get(id=tid)
        form=StudentForm(initial={"roll_no":task.roll_no,"name":task.name,"cource":task.cource,"subject":task.subject,"phone_no":task.phone_no})
        return render(request,"edit.html",{"form":form})
    def post(self,request,**kwargs):
        formdata=StudentForm(data=request.POST)
        tid=kwargs.get('id')
        task=Students.objects.get(id=tid)
        if formdata.is_valid():
            roll_no=formdata.cleaned_data.get('roll_no')
            name=formdata.cleaned_data.get('name')
            cource=formdata.cleaned_data.get('cource')
            subject=formdata.cleaned_data.get('subject')
            phone_no=formdata.cleaned_data.get('phone_no')
            task.roll_no=roll_no
            task.name=name
            task.cource=cource
            task.subject=subject
            task.phone_no=phone_no
            task.save()
            return redirect('dash')
        return render(request,"edit.html",{"form":formdata})   

class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request):
        formdata=RegForm(data=request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('log')
        return render(request,"reg.html",{"form":formdata}) 



