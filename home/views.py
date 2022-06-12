from cmath import pi
from email.policy import default
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from home.forms import MemberRegistration, CreateUserForm, EquipmentRegistration
from home.models import Equipments, Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def addmembers(request):
    context= {'success': False, 'name':'sar'}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['birthday']
        occupation = request.POST['occupation']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        plan = request.POST['plan']
        shift = request.POST['shift']
        
        #print(name, email, dob, occupation, phone, address, city, state, zip, plan, shift)
        ins = Member(
        name=name, 
        email=email, 
        dob=dob, 
        occupation=occupation, 
        phone=phone,
        address=address,
        city=city,
        state=state, 
        zip=zip,
        plan=plan, 
        shift=shift,
        
        )
        ins.save()
        context= {'success': True}

    return render(request,'addmembers.html', context)

@login_required(login_url='login')
def members(request):
    all_members = Member.objects.all()
    # print(all_members)
    # for item in all_members:
    #     print(item.name)
    context = {'members': all_members}

    return render(request,'members.html', context)

@login_required(login_url='login')
def update(request, member_id):
    if request.method == 'POST':
        pi=Member.objects.get(pk=member_id)
        fm = MemberRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi = Member.objects.get(pk=member_id)
            fm = MemberRegistration(instance=pi)

    
    return render(request, 'update.html', {'form':fm})
        
@login_required(login_url='login')
def delete_data(request, member_id):
    if request.method=='POST':
        pi= Member.objects.get(pk=member_id)
        pi.delete()
        context= {'success': True}
        return HttpResponseRedirect('/members')

def loginpage(request):
    if request.user.is_authenticated:
       return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else: 
                messages.info(request, 'Username or password is incorrect')
            



    context = {}
    return render(request, 'login.html' , context)

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        
    context = {'form':form} 
    return render(request, 'register.html' , context)

def logoutUser(request):
    logout(request)
    return redirect ('login')



def equipments(request):
    if request.method == 'POST':
        fm = EquipmentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = EquipmentRegistration()
    else:
        fm = EquipmentRegistration()
    eq = Equipments.objects.all()
    return render(request,'equipments.html', {'form':fm, 'equ':eq})

def eq_delete_data(request, equi_id):
    if request.method=='POST':
        pi= Equipments.objects.get(pk=equi_id)
        pi.delete()
        return HttpResponseRedirect('/equipments')



    