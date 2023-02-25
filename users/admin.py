from django.contrib import admin

from users.models import Profile,Skills,Message

# Register your models here.


admin.site.register(Profile)
admin.site.register(Skills)
admin.site.register(Message)
