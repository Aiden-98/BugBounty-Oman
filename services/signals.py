from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ServicesRequest, ServicesRequestParticipant, Awards


# def addServicesRequest(sender, instance, created, **kwargs):
#     profile=instance
#     user = profile.user
#     if created == False:
#         user.first_name = profile.CuRes_Contact_Person
#         user.username=profile.CuRes_Org_Name
#         user.email = profile.CuRes_Email
#         user.save()


# post_save.connect(cyCreateProfile, sender=User)
# post_save.connect(cyUpdateUser, sender=cyProfile)
# post_save.connect(cuUpdateUser, sender=customerProfile)
# post_delete.connect(DeleteUser, sender=cyProfile) 
# post_delete.connect(DeleteUser, sender=customerProfile) 