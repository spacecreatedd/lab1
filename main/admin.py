from django.contrib import admin
from .models import Choice
from .models import Post

admin.site.register(Post)
admin.site.register(Choice)