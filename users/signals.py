from django.db.models.signals import  post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

def CreateProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile =Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name)
        
        subject = 'Welcome to my Site'
        message = 'this is best site'
        send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False
            )
            
            
post_save.connect(CreateProfile,sender=User)