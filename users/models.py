import users
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class cyProfile(models.Model):

    CyResTypeOption=(
        ('Government', 'Government'),
        ('Priavte', 'Priavte'),
        ('Both', 'Both'),
    )

    cy_status=(
        ('accepted', 'accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    CyRes_UserName = models.CharField(max_length=225, null=True, blank=True)
    CyRes_Name = models.CharField(max_length=225, null=True, blank=True)
    CyRes_Email=models.EmailField(max_length=500, null=True, blank=True)
    #CyRes_Country=models.coun
    CyRes_Phone= models.CharField(max_length=50)
    CuRes_Status=models.CharField(max_length=225,null=True, blank=True, choices=cy_status, default='Pending') #If you change the CuRes_Status to CyRes_Status, you have to change the same in the whole project.
    CyRes_Bio=models.TextField(null=True, blank=True)
    CyRes_Profile_Image=models.ImageField(null=True, blank=True, default='Profile_Icon.png')
    CyRes_Service_Type=models.CharField(max_length=225, choices=CyResTypeOption, null=True, blank=True)
    CyRes_Documents=models.FileField(null=True, blank=True)
    CyRes_Start_Date=models.CharField(max_length=500, null=True, blank=True)
    CyRes_Note=models.CharField(max_length=225,null=True, blank=True)


    CyRes_Created =models.DateTimeField(auto_now_add=True)
    CyRes_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.CyRes_UserName



class customerProfile(models.Model):

    CuResTypeOption=(
        ('Government', 'Government'),
        ('Priavte', 'Priavte'),
    )
    cu_status=(
        ('accepted', 'accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    CuRes_Org_Name = models.CharField(max_length=225, null=True, blank=True)
    CuRes_Contact_Person = models.CharField(max_length=225, null=True, blank=True)
    CuRes_Contact_Designation=models.CharField(max_length=225, null=True, blank=True)
    CuRes_Email= models.EmailField(max_length=500, null=True, blank=True)
    CuRes_Phone=models.CharField(max_length=225,null=True, blank=True)
    CuRes_Status=models.CharField(max_length=225,null=True, blank=True, choices=cu_status, default='Pending')
    CuRes_Profile_Image=models.ImageField(null=True, blank=True, default='Profile_Icon.png')
    CuRes_Description=models.TextField(null=True, blank=True)
    CuRes_organization_Sector=models.CharField(max_length=225, choices=CuResTypeOption, null=True, blank=True)
    CuRes_Start_Date=models.CharField(max_length=500, null=True, blank=True)
    CuRes_Documents=models.FileField(null=True, blank=True)
    CuRes_Note=models.CharField(max_length=225,null=True, blank=True)

    
    CuRes_Created =models.DateTimeField(auto_now_add=True)
    CuRes_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.CuRes_Org_Name


class Cus_LOGS(models.Model):
    
    Cus_LOG_Status=models.CharField(max_length=225, null=True, blank=True)
    Cus_LOG_Sector=models.CharField(max_length=225, null=True, blank=True)
    Cus_LOG_Note=models.CharField(max_length=225, null=True, blank=True)
    Cus_LOG_User=models.CharField(max_length=225, null=True, blank=True)

    CuRes_ID=models.ForeignKey(customerProfile, on_delete=models.CASCADE, null=True, blank=True)
    Cus_LOG_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Cus_Created =models.DateTimeField(auto_now_add=True)

class Cy_LOGS(models.Model):
    
    Cy_LOG_Status=models.CharField(max_length=225, null=True, blank=True)
    Cy_LOG_Sector=models.CharField(max_length=225, null=True, blank=True)
    Cy_LOG_Note=models.CharField(max_length=225, null=True, blank=True)
    Cy_LOG_User=models.CharField(max_length=225, null=True, blank=True)

    CyRes_ID=models.ForeignKey(cyProfile, on_delete=models.CASCADE, null=True, blank=True)
    Cy_LOG_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Cy_Created =models.DateTimeField(auto_now_add=True)
