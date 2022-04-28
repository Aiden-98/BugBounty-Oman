from django.db import models
from django.contrib.auth.models import User
from users.models import cyProfile, customerProfile
import uuid
# Create your models here.
class ServicesRequest(models.Model):
    
    Status=(
        ('Accepted', 'Accepted'),
        ('Witing_for_Pyament', 'Witing for Pyament'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Closed','Closed'),

    )
    
    SR_Organization_Name=models.CharField(max_length=225, null=True, blank=True)
    SR_Type=models.CharField(max_length=225, null=True, blank=True)
    SR_URL=models.CharField(max_length=2000, null=True, blank=True)
    SR_Approval_status=models.CharField(max_length=225, null=True, blank=True,choices=Status, default="Pending")
    SR_Description=models.TextField(null=True, blank=True)
    SR_Low_Award=models.CharField(max_length=225, null=True, blank=True)
    SR_Medium_Award=models.CharField(max_length=225, null=True, blank=True)
    SR_High_Award=models.CharField(max_length=225, null=True, blank=True)
    SR_Critical_Award=models.CharField(max_length=225, null=True, blank=True)
    SR_Package=models.CharField(max_length=225, null=True, blank=True)
    SR_Note=models.CharField(max_length=225, null=True, blank=True)

    CuRes_ID=models.ForeignKey(customerProfile, on_delete=models.CASCADE, null=True, blank=True)
    SR_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    SR_Created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.SR_Organization_Name

    
class ServicesRequestParticipant(models.Model):
    
    SRP_status=(
        ('accepted', 'accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),

    )
    SRP_scores=(
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    )


    
    
    SRP_Organization_Name=models.CharField(max_length=225, null=True, blank=True)
    SRP_Services_Type=models.CharField(max_length=225, null=True, blank=True)
    SRP_Title=models.CharField(max_length=225, null=True, blank=True)
    SRP_Description=models.TextField(null=True, blank=True)
    SRP_Report=models.FileField(null=True, blank=True)
    SRP_Status=models.CharField(max_length=225, null=True, blank=True, choices=SRP_status, default="Pending")
    SRP_Note=models.CharField(max_length=225, null=True, blank=True)

    SRP_Loss_of_Confidentiality=models.CharField(max_length=225, null=True, blank=True, choices=SRP_scores)
    SRP_Loss_of_Integrity=models.CharField(max_length=225, null=True, blank=True, choices=SRP_scores)
    SRP_Loss_of_Availability=models.CharField(max_length=225, null=True, blank=True, choices=SRP_scores)
    SRP_Loss_of_Accountability=models.CharField(max_length=225, null=True, blank=True, choices=SRP_scores)
    SRP_Total=models.CharField(max_length=225, null=True, blank=True)
    SRP_Danger=models.CharField(max_length=225, null=True, blank=True)

    SR_ID=models.ForeignKey(ServicesRequest, on_delete=models.CASCADE, null=True, blank=True)
    CyRes_ID=models.ForeignKey(cyProfile, on_delete=models.CASCADE, null=True, blank=True)
    SRP_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    SRP_Created =models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.SRP_Organization_Name

    
class Awards(models.Model):

    SRA_scores=(
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    )    
    
    SRA_Organization_Name=models.CharField(max_length=225, null=True, blank=True)
    CyRes_UserName=models.CharField(max_length=225, null=True, blank=True)
    SRA_Danger_Of_Vuln=models.CharField(max_length=225, null=True, blank=True)
    SRA_prize=models.CharField(max_length=225, null=True, blank=True)
    SRA_Note=models.CharField(max_length=225, null=True, blank=True)
    SRA_User_Created=models.CharField(max_length=225, null=True, blank=True)


    SRA_Loss_of_Confidentiality=models.CharField(max_length=225, null=True, blank=True, choices=SRA_scores, default="Low")
    SRA_Loss_of_Integrity=models.CharField(max_length=225, null=True, blank=True, choices=SRA_scores, default="Low")
    SRA_Loss_of_Availability=models.CharField(max_length=225, null=True, blank=True, choices=SRA_scores, default="Low")
    SRA_Loss_of_Accountability=models.CharField(max_length=225, null=True, blank=True, choices=SRA_scores, default="Low")
    SRA_Technical_Total=models.CharField(max_length=225, null=True, blank=True)

    SRA_Financial_Damage=models.CharField(max_length=225, null=True, blank=True, choices=SRA_scores, default="Low")
    SRA_Privacy_Violation=models.CharField(max_length=225, null=True, blank=True, choices=SRA_scores, default="Low")
    SRA_Reputational_Damage=models.CharField(max_length=225, null=True, blank=True, choices=SRA_scores, default="Low")
    SRA_Business_Total=models.CharField(max_length=225, null=True, blank=True)
    
    SRP_ID=models.ForeignKey(ServicesRequestParticipant, on_delete=models.CASCADE, null=True, blank=True)
    SRA_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    SRA_Created =models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.SRA_Organization_Name

    

class SR_LOGS(models.Model):
    
    SR_LOG_Status=models.CharField(max_length=225, null=True, blank=True)
    SR_LOG_User=models.CharField(max_length=225, null=True, blank=True)

    SR_ID=models.ForeignKey(ServicesRequest, on_delete=models.CASCADE, null=True, blank=True)
    SR_LOG_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    SRA_Created =models.DateTimeField(auto_now_add=True)


class SRP_LOGS(models.Model):
    
    SRP_LOG_Status=models.CharField(max_length=225, null=True, blank=True)
    SRP_LOG_User=models.CharField(max_length=225, null=True, blank=True)
    SRP_Note=models.CharField(max_length=225, null=True, blank=True)

    SRP_LOG_Loss_of_Confidentiality=models.CharField(max_length=225, null=True, blank=True)
    SRP_LOG_Loss_of_Integrity=models.CharField(max_length=225, null=True, blank=True)
    SRP_LOG_Loss_of_Availability=models.CharField(max_length=225, null=True, blank=True)
    SRP_LOG_Loss_of_Accountability=models.CharField(max_length=225, null=True, blank=True)
    SRP_LOG_Technical_Total=models.CharField(max_length=225, null=True, blank=True)
    SRP_LOG_Danger=models.CharField(max_length=225, null=True, blank=True)

    SRP_ID=models.ForeignKey(ServicesRequestParticipant, on_delete=models.CASCADE, null=True, blank=True)
    SRP_LOG_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    SRP_Created =models.DateTimeField(auto_now_add=True)



class Report_Bug(models.Model):

    Re_status=(
        ('Accepted', 'Accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),

    )

    Re_UserName=models.CharField(max_length=225, null=True, blank=True)
    Re_Phone=models.CharField(max_length=225, null=True, blank=True)
    Re_Email=models.CharField(max_length=225, null=True, blank=True)
    Re_Title=models.CharField(max_length=225, null=True, blank=True)
    Re_Description=models.TextField(null=True, blank=True)
    Re_Report=models.FileField(null=True, blank=True)
    Re_Status=models.CharField(max_length=225, null=True, blank=True, choices=Re_status, default="Pending")

    CyRes_ID=models.ForeignKey(cyProfile, on_delete=models.CASCADE, null=True, blank=True)
    Re_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Re_Created =models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.Re_UserName

    


class ReBug_LOGS(models.Model):
    
    ReBug_LOG_Status=models.CharField(max_length=225, null=True, blank=True)
    ReBug_LOG_User=models.CharField(max_length=225, null=True, blank=True)

    Re_ID=models.ForeignKey(Report_Bug, on_delete=models.CASCADE, null=True, blank=True)
    ReBug_LOG_ID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ReBug_Created =models.DateTimeField(auto_now_add=True)

