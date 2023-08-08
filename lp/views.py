from django.http import HttpResponse # ai module ta amak function er moddhe kono kisu return korte hole help korbe
import datetime
from django.shortcuts import render # ai render module ta amak html template ta ke use korte help korbe
from django.shortcuts import redirect
from articles.models import signup
from articles.models import upload_picture
def home(request):
    # return HttpResponse("This is the Homepage & it's urls name is home/")
    return render(request,'homepage.html')

def cse(request):
    x=['Himel','Tanvir'] #aikhane akta list create kora hoyese
    # return HttpResponse("I am studying in CSE")
    return render(request,'cse.html',{'dict':x,})

def button(request):
    return render(request,'extends.html')


def contact(request):
    return render(request,'contact.html')

def sign_up(request):
    if request.method =='POST':
        es=request.POST['email']
        ps=request.POST['password']
        us=request.POST['username']
        obj1 = signup(email=es,password=ps,username=us)
        obj1.save()
        #if request.method =='POST':
            #pl=request.POST['pswd']
            #el=request.POST['mail']
            #for i in range(15):
                #obj2=signup.objects.get(id=i+1)
                #if(obj2.email==el and obj2.password==pl):
                    #return redirect('http://127.0.0.1:8000/main/')
                    #break
        #obj2=signup.objects.get(id=1)
    return render(request,'login.html')

#def log_in(request):
    #if request.method == 'POST':
        #el=request.POST['email']
        #pl=request.POST['password']

def profile(request):
    return render(request,'profile.html')

def upload(request):
    if request.method == 'POST':
        img=request.POST['image']
        obj2 = upload_picture(image=img)
        obj2.save()
    return render(request,'j.upload.html')

def shop_now(request):
    return render(request,'shop_now.html')

def checkout(request):
    return render(request,'add_num_button.html')

def about(request):
    return render(request,'aboutus.html')