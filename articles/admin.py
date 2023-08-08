from django.contrib import admin
from.models import Article
from.models import signup
from.models import upload_picture

#register kora lagbe model gulo
admin.site.register(Article)
admin.site.register(signup)
admin.site.register(upload_picture)

