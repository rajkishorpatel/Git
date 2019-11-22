from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

def form_view(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'GitApp/git.html',{'form':form})


