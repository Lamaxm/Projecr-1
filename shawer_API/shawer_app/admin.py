from django.contrib import admin
from .models import comment, courses

list_display = ['id', 'username']

admin.site.register(comment)
admin.site.register(courses)
