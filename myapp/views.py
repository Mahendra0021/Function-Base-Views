from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StudentForm
from .models import Student

def add_show(request):
    print("mahendra")
    if request.method == 'POST':
        Uname = request.POST['Uname']
        email = request.POST['email']
        password =request.POST['password']
        student = Student(Uname=Uname, email=email, password=password)
        student.save()
        return redirect('/')
    else:
        fm = StudentForm()
        data = Student.objects.all()
    return render(request, 'add_and_data_show.html', {'form': fm, 'data':data})

def update(request, id):
    if request.method == 'POST':
        Uname = request.POST.get('Uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        update_data = Student.objects.get(id=id)
        update_data.Uname = Uname
        update_data.email = email
        update_data.password = password
        update_data.save()
    else:
        update_data = Student.objects.get(id=id)
    return render(request, 'update.html', {'update_data': update_data})


def delete(request,id):
    i = Student.objects.get(pk=id)
    i.delete()
    return HttpResponseRedirect('/')