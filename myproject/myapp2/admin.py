from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import User, UserProfile, Notice, Book

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Notice)
admin.site.register(Book)