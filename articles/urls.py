#from django.contrib import admin #aikhane admin section ta na thakleo hobe,karon main  default app a admin section ase.
from django.urls import path
from .import views

urlpatterns = [
    #path('admin/', admin.site.urls),# aikhane amader admin url dorkar nai
    path('',views.article_list),# Empty urle create kora hoise
    #path('about/',views.cse) # amader ai url tao dorkar nai 
]