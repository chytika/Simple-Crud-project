from django.shortcuts import render,HttpResponseRedirect
from .forms import NewStudent
from .models import Student

# Create your views here.

def addshow(request):
    if request.method == 'POST':
        fm = NewStudent(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm, email=em, password=pw)
            reg.save()
            fm = NewStudent() 
    else:
        fm = NewStudent() 
    std = Student.objects.all()   
    return render(request,'enroll/addandshow.html', {'form': fm, 'stu': std})

def update(request, id):
 if request.method == "POST":
    pi = Student.objects.get(pk=id)
    fm = NewStudent(request.POST, instance=pi)
    if fm.is_valid():
     fm.save()
 else:
    pi = Student.objects.get(pk=id)
    fm = NewStudent(instance=pi)
    return render(request,'enroll/updatestudent.html', {'form':fm})

def delete(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')