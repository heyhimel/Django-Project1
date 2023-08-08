from django.shortcuts import render
from .models import Article
from .models import signup

# Create your views here.
def article_list(request):
    art=Article.objects.all() # aikhane amra akta object create korlam jar name dilam "art"
    art1=Article.objects.all()
    
    return render(request,'articles/article_list.html',{'dictionary':art,'dictionary1':art1})
# Aikhane comma er pore '/' er ag porjonto brase er moddhe  
# Articles lekha holo,Aita amader Django app tar nam
# Ai Django app er nam na lekha hole django confused hoye jeto
# aikhane render er moddhe 2nd bracket er moddhe dictionary use kore variable access kora hosse

