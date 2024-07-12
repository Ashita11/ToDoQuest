from django.shortcuts import render,redirect
from tkinter import *
from tkinter import messagebox
from todoapp.models import *
from datetime import date, timedelta
from urllib.parse import urlencode
from django.urls import reverse

def index(req):
    
    try:
        if 'user' in req.session.keys():
            id = req.session['user']
            s1=user.objects.get(id=id)
            data = {'uid': id, 'name':s1.name}
            url = f"{reverse('home')}?{urlencode(data)}"
            return redirect(url)
        else:
            if(req.method == 'POST'):
                email = req.POST['email']
                s1=user.objects.get(email=email)
                if(s1.password == req.POST['password']):
                    lists = listitem.objects.filter(user_id=s1.id)
                    task = tasks.objects.filter(user_id=s1.id)
                    req.session['user']=s1.id
                    return render(req,'home.html',{'lists':lists,'task':task, 'uid':s1.id, 'name':s1.name})
                else:
                    root1=Tk()
                    root1.withdraw()
                    root1.attributes('-topmost',True)
                    messagebox.showerror('incorrect password','The entered password does not match with the email')
                    return redirect('index')
    except Exception as e: 
        root=Tk()
        root.withdraw()
        root.attributes('-topmost',True)
        messagebox.showerror('invalid','this email is not registered with us')
        return redirect('index')
    return render(req,'index.html')

def signup(req):
    if 'user' in req.session.keys():
            id = req.session['user']
            s1=user.objects.get(id=id)
            data = {'uid': id, 'name':s1.name}
            url = f"{reverse('home')}?{urlencode(data)}"
            return redirect(url)
    else:
        if(req.method == 'POST'):
            email=req.POST['email']
            s=user.objects.all()
            for i in s:
                if(i.email == email):
                    root1=Tk()
                    root1.withdraw()
                    root1.attributes('-topmost',True)
                    messagebox.showerror('','This email is already registered with us')
                    return redirect('signup')
            name=req.POST['username']
            pswd=req.POST['password']
            s1=user(name=name,email=email,password=pswd)
            s1.save()
            req.session['user']=s1.id
            lists = listitem.objects.filter(user_id=s1.id)
            task = tasks.objects.filter(user_id=s1.id)
            return render(req,'home.html',{'lists':lists,'task':task, 'uid':s1.id, 'name':s1.name})
    return render(req,'signup.html')

def home(req):
    if 'user' in req.session.keys():
        # id = req.GET.get("uid")
        id = req.session['user']
        # name = req.GET.get("name")
        s1=user.objects.get(id=id)
        lists = listitem.objects.filter(user_id=id)
        task = tasks.objects.filter(user_id=id)
        return render(req,'home.html',{'lists':lists,'task':task, 'uid':id, 'name':s1.name})
    else:
        return render(req,'index.html')
    

def savelist(req):
    id = req.POST.get('id')
    name= req.POST.get('name')
    s1_instance = user.objects.get(id=id)
    s = listitem(name=req.POST['cat'], user_id=s1_instance.id)
    s.save()
    data = {'uid': id, 'name':name}
    url = f"{reverse('home')}?{urlencode(data)}"
    return redirect(url)

def savetasks(req):
    id=req.POST.get('id')
    name=req.POST.get('name')
    s1_instance = user.objects.get(id=id)
    listid = req.POST.get('list_id')
    pri = req.POST.get('pri')
    list_instance = listitem.objects.get(id=listid, user_id=s1_instance.id)
    s = tasks(list=list_instance, user_id=s1_instance.id, name=req.POST['task'], desc=req.POST['desc'], priority=pri, due_date=req.POST['due'])
    s.save()
    data = {'uid': id, 'name': name}
    url = f"{reverse('home')}?{urlencode(data)}"
    return redirect(url)
    # return redirect('home')

def delete(req):
    id=req.POST.get('id')
    name=req.POST.get('name')
    s1=listitem.objects.get(id=req.POST.get('list_id'))
    s1.delete()
    data = {'uid': id, 'name': name}
    url = f"{reverse('home')}?{urlencode(data)}"
    return redirect(url)

def display(req):
    id =req.GET['uid']
    idl = req.GET['idl']
    s1_instance = user.objects.get(id=id)
    nm=idl
    today = date.today()
    li={'name':idl,"id":idl}
    if idl=="Upcoming":
        print("hello2")
        task=tasks.objects.filter(due_date__gte=today, due_date__lte=today + timedelta(days=7),completed=0, user_id=s1_instance.id)
        return render(req,'display.html',{'task':task,'li':li,'uid':id})
    elif idl=="Today":
        task=tasks.objects.filter(due_date=today,completed=0, user_id=s1_instance.id)
        return render(req,'display.html',{'task':task,'li':li,'uid':id})
    elif idl=="Missed":
        task=tasks.objects.filter(due_date__lt=today, completed=0, user_id=s1_instance.id)
        return render(req,'display.html',{'task':task,'li':li,'uid':id})
    elif idl=="All Tasks":
        task=tasks.objects.filter(completed=0, user_id=s1_instance.id)
        return render(req,'display.html',{'task':task,'li':li,'uid':id})
    else:
        li=listitem.objects.get(id=idl,user_id=s1_instance.id)
        nm=li.name
        print(nm)
        task = tasks.objects.filter(list_id=idl,completed=0, user_id=s1_instance.id)
    return render(req,'display.html',{'task':task,'li':li,'uid':id})

def complete(req):
    id=req.GET['id']
    uid=req.GET['uid']
    nm=req.GET['nm']
    s1_instance=user.objects.get(id=uid)
    task=tasks.objects.get(id=id,user_id=s1_instance.id)
    task.completed=1
    task.save()
    data = {'uid': uid, 'idl': nm}
    url = f"{reverse('display')}?{urlencode(data)}"
    return redirect(url)
    # data = {'uid': uid, 'name': s1_instance.name}
    # url = f"{reverse('home')}?{urlencode(data)}"
    # return redirect(url)
    # return redirect('home')

def delTask(req):
    id=req.GET['id']
    uid=req.GET['uid']
    nm=req.GET['nm']
    s1_instance=user.objects.get(id=uid)
    print(s1_instance.name)
    task=tasks.objects.get(id=id,user_id=s1_instance.id)
    task.delete()
    data = {'uid': uid, 'idl': nm}
    url = f"{reverse('display')}?{urlencode(data)}"
    return redirect(url)
    # data = {'uid': uid, 'name': s1_instance.name}
    # url = f"{reverse('home')}?{urlencode(data)}"
    # return redirect(url)

def delTaskC(req):
    id=req.GET['id']
    uid=req.GET['uid']
    nm=req.GET['nm']
    s1_instance=user.objects.get(id=uid)
    print(s1_instance.name)
    task=tasks.objects.get(id=id,user_id=s1_instance.id)
    task.delete()
    data = {'uid': uid, 'idl': nm}
    url = f"{reverse('completed')}?{urlencode(data)}"
    return redirect(url)

def completed(req):
    id =req.GET['uid']
    idl = req.GET['idl']
    s1_instance = user.objects.get(id=id)
    nm=idl
    task=tasks.objects.filter(completed=1, user_id=s1_instance.id)
    return render(req,'completed.html',{'task':task,'nm':nm,'uid':id})

def details(req):
    id = req.GET['id']
    uid = req.GET['uid']
    task = tasks.objects.get(id=id)
    return render(req, 'task_details.html', {'task': task,'uid':uid})


def logout(req):
    if 'user' in req.session.keys():
        del req.session['user']
        return redirect('index')
    return redirect('index')