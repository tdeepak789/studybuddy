from django.contrib import admin
# from .models import Room
from .models import Topic,Room,Message,User
# Register your models here.
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(User)