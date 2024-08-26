from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.http import HttpResponse

def home(request):
    return render(request,'webapp/index.html')

#register

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
        
    context ={'form':form}
    
    return render(request,'webapp/register.html',context)

# - login 

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            
    context = {'form2':form}
    
    return render(request,'webapp/my-login.html',context)


@login_required(login_url='my_login')
def dashboard(request):
    my_records = Record.objects.all()
    
    context = {'records':my_records}

    return render(request,'webapp/dashboard.html',context=context)

# create a record


@login_required(login_url='my_login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()


            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)



def user_logout(request):
    auth.logout(request)
    return redirect('my-login')