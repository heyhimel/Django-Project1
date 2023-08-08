"""lp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
from .views import sign_up
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),# aikhane first bracket er moddhe comma er age jei lekha tuku ase 
                         #aitai amader local server er addrees er sheshe add hoye akta url create kore
                         #comma er age jodi ami kono curlibrase er moddhe kisu na dei tahole aitar url empty url hobe
                         #tokhon just local server er ip address run klorale home function call hobe
    path('about/',views.about),
    path('mains/',views.button),
    path('articles/',include('articles.urls')),
    # Aikhane django te jei notun "articles" app ta create kora hoise sheitar url ta 
    # Main default app er mooddhe include kora hoise.
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('upload/',views.upload),
    path('',views.sign_up),
    path('shop_now/',views.shop_now),
    path('shop_now/checkout/',views.checkout)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns() #aikhane static file er jonno url ke request er jonno ai funtion ta create kora holo
