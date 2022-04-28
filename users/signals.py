from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import cyProfile,customerProfile
from django.core.mail import send_mail
from django.conf import settings

#@receiver(post_save, sender=cyProfile)
def cyCreateProfile(sender, instance, created, **kwargs):
    print('User created!')
    if created:
        user=instance
        if str(user.last_name) == 'cy':
            profile=cyProfile.objects.create(
                user=user,
                CyRes_UserName=user.username,
                CyRes_Email=user.email,
                CyRes_Name=user.first_name,
            )


            send_mail(
                'Welcome to BugBountyOman',
                'welcome to Bugbounty Oman \n The most comprehensive and up to date security vulnerability disclosure platform\n Helps you to secure the application that powers your organization',
                settings.EMAIL_HOST_USER,
                 [profile.CyRes_Email],
                fail_silently=False,

            )

        elif str(user.last_name) == 'org':
            profile=customerProfile.objects.create(
                user=user,
                CuRes_Org_Name=user.username,
                CuRes_Email=user.email,
                CuRes_Contact_Person=user.first_name,
            )
    

def DeleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


def cyUpdateUser(sender, instance, created, **kwargs):
    profile=instance
    user = profile.user
    if created == False:
        user.first_name = profile.CyRes_Name
        user.username=profile.CyRes_UserName
        user.email = profile.CyRes_Email
        user.save()

def cuUpdateUser(sender, instance, created, **kwargs):
    profile=instance
    user = profile.user
    if created == False:
        user.first_name = profile.CuRes_Contact_Person
        user.username=profile.CuRes_Org_Name
        user.email = profile.CuRes_Email
        user.save()

post_save.connect(cyCreateProfile, sender=User)
post_save.connect(cyUpdateUser, sender=cyProfile)
post_save.connect(cuUpdateUser, sender=customerProfile)
post_delete.connect(DeleteUser, sender=cyProfile) 
post_delete.connect(DeleteUser, sender=customerProfile) 