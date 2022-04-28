from django.db.models import fields
from django.forms import ModelForm
from .models import ServicesRequest, ServicesRequestParticipant, Awards, SR_LOGS, SRP_LOGS, Report_Bug, ReBug_LOGS
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import cyProfile,customerProfile, Cus_LOGS, Cy_LOGS

from django import forms

class addSRForm(ModelForm):
    class Meta:
        model = ServicesRequest
        fields =['SR_Organization_Name','SR_Type','SR_URL','SR_Description','SR_Low_Award','SR_Medium_Award','SR_High_Award','SR_Critical_Award','CuRes_ID', 'SR_Package']
        exclude = ("CuRes_ID","SR_Organization_Name","SR_Type","SR_Package")
        labels={
            'SR_Organization_Name':'Organization Name',
            'SR_URL':'Website Link',
            'SR_Description':'Description',
            'SR_Low_Award':'Low Award',
            'SR_Medium_Award':'Medium Award',
            'SR_High_Award':'High Award',
            'SR_Critical_Award':'Critical Award'
        }

    def __init__(self,*args,**kwargs):
        super(addSRForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class SRPForm(ModelForm):
    class Meta:
        model = ServicesRequestParticipant
        fields =['SRP_Title','SRP_Description','SRP_Report','SRP_Loss_of_Confidentiality','SRP_Loss_of_Integrity','SRP_Loss_of_Availability','SRP_Loss_of_Accountability','SRP_Total','SR_ID','CyRes_ID','SRP_Danger']
        exclude = ("SR_ID","CyRes_ID","SRP_Total","SRP_Danger")
        labels={
            'SRP_Title':'Title',
            'SRP_Description':'Description',
            'SRP_Report':'Upload File (Report/Media)',
            'SRP_Loss_of_Confidentiality':'Loss of Confidentiality',
            'SRP_Loss_of_Integrity':'Loss of Integrity',
            'SRP_Loss_of_Availability':'Loss of Availability',
            'SRP_Loss_of_Accountability':'Loss of Accountability',

        }
        # widgets = {
        #     'SRP_Loss_of_Confidentiality': forms.RadioSelect(),
        #     'SRP_Loss_of_Integrity': forms.RadioSelect(),
        #     'SRP_Loss_of_Availability': forms.RadioSelect(),
        #     'SRP_Loss_of_Accountability': forms.RadioSelect(),

        # }   

    def __init__(self,*args,**kwargs):
        super(SRPForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        self.fields['SRP_Description'].initial = 'Follow the description sample.'
        # self.fields['SRP_Loss_of_Confidentiality'].widget.attrs.update({'class': 'btn btn-light form-control btn-group-vertical mb-2'})
        # self.fields['SRP_Loss_of_Integrity'].widget.attrs.update({'class': 'btn btn-light form-control btn-group-vertical mb-2'})
        # self.fields['SRP_Loss_of_Availability'].widget.attrs.update({'class': 'btn btn-light form-control btn-group-vertical mb-2'})
        # self.fields['SRP_Loss_of_Accountability'].widget.attrs.update({'class': 'btn btn-light form-control btn-group-vertical mb-2'})



class AwardsForm(ModelForm):
    class Meta:
        model = Awards
        fields =['SRA_prize','SRA_Danger_Of_Vuln']
        exclude = ('SRA_Danger_Of_Vuln','SRA_prize')
        labels={

        }     
    def __init__(self,*args,**kwargs):
        super(AwardsForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        
#Aadmin Tables


class Admin_CyProForm(ModelForm):
    class Meta:
        model = cyProfile
        fields =['CyRes_Name','CyRes_Bio','CyRes_Profile_Image','CyRes_Service_Type','CyRes_Documents','CuRes_Status','CyRes_Note']
        exclude = ('CyRes_Name','CyRes_Bio','CyRes_Profile_Image','CyRes_Documents')
        labels={
            'CyRes_Service_Type':'Type',
            'CyRes_Documents':'Documents',
            'CuRes_Status':'Status',
            'CyRes_Note':'Note'
        }

    def __init__(self,*args,**kwargs):
        super(Admin_CyProForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        

class Admin_CuProForm(ModelForm):
    class Meta:
        model = customerProfile
        fields =['CuRes_Org_Name','CuRes_Contact_Person','CuRes_Contact_Designation','CuRes_Email','CuRes_Phone','CuRes_Profile_Image','CuRes_Description','CuRes_organization_Sector', 'CuRes_Documents','CuRes_Status','CuRes_Note']
        exclude = ('CuRes_Org_Name','CuRes_Contact_Person','CuRes_Contact_Designation','CuRes_Email','CuRes_Phone','CuRes_Profile_Image','CuRes_Description','CuRes_Documents')    
        labels={

            'CuRes_organization_Sector':'Organization Sector',
            'CuRes_Documents':'Documents',
            'CuRes_Status':'Status',
            'CuRes_Note': 'Note'
            
        }


    def __init__(self,*args,**kwargs):
        super(Admin_CuProForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        

class Admin_SRForm(ModelForm):
    class Meta:
        model = ServicesRequest
        fields =['SR_Type','SR_URL','SR_Description','SR_Low_Award','SR_Medium_Award','SR_High_Award','SR_Critical_Award','CuRes_ID','SR_Approval_status','SR_Note']
        labels={
            'SR_Type':'Type',
            'SR_URL':'Website Link',
            'SR_Description':'Description',
            'SR_Low_Award':'Low Award',
            'SR_Medium_Award':'Medium Award',
            'SR_High_Award':'High Award',
            'SR_Critical_Award':'Critical Award',
            'CuRes_ID':'Organization Name',
            'SR_Approval_status':'Status',
            'SR_Note':'Note'
        }

    def __init__(self,*args,**kwargs):
        super(Admin_SRForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class Admin_SRPForm(ModelForm):
    class Meta:
        model = ServicesRequestParticipant
        fields =['SR_ID','CyRes_ID','SRP_Status','SRP_Loss_of_Confidentiality','SRP_Loss_of_Integrity','SRP_Loss_of_Availability','SRP_Loss_of_Accountability','SRP_Total','SRP_Danger','SRP_Note']
        exclude = ("SR_ID","CyRes_ID","SRP_Total","SRP_Danger")
        labels={
            'SRP_Status':'Status',
            'SRP_Note':'Note',
            'SRP_Loss_of_Confidentiality':'Loss of Confidentiality',
            'SRP_Loss_of_Integrity':'Loss of Integrity',
            'SRP_Loss_of_Availability':'Loss of Availability',
            'SRP_Loss_of_Accountability':'Loss of Accountability',


        }
        # widgets = {
        #     'SRP_Loss_of_Confidentiality': forms.RadioSelect(),
        # }        

    def __init__(self,*args,**kwargs):
        super(Admin_SRPForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class Admin_Cy_LOGS(ModelForm):
    class Meta:
        model = Cy_LOGS
        fields =['Cy_LOG_Status','Cy_LOG_Sector','Cy_LOG_User','Cy_LOG_Note']
        labels={
            'Cy_LOG_Status':'Status',
            'Cy_LOG_Sector':'Sector',
            'Cy_LOG_Note':'Note',
            'Cy_LOG_User':'User',
          
        }

class Admin_Cus_LOGS(ModelForm):
    class Meta:
        model = Cus_LOGS
        fields =['Cus_LOG_Status','Cus_LOG_Sector','Cus_LOG_User','Cus_LOG_Note']
        labels={
            'Cus_LOG_Status':'Status',
            'Cus_LOG_Sector':'Sector',
            'Cus_LOG_Note':'Note',
            'Cus_LOG_User':'User',
          
        }



class Admin_SR_LOGS(ModelForm):
    class Meta:
        model = SR_LOGS
        fields =['SR_LOG_Status','SR_LOG_User']
        labels={
            'SR_LOG_Status':'Status',
            'SR_LOG_User':'User',
          
        }

class Admin_SRP_LOGS(ModelForm):
    class Meta:
        model = SRP_LOGS
        fields =['SRP_LOG_Status','SRP_LOG_User','SRP_LOG_Loss_of_Confidentiality','SRP_LOG_Loss_of_Integrity','SRP_LOG_Loss_of_Availability','SRP_LOG_Loss_of_Accountability','SRP_LOG_Technical_Total','SRP_LOG_Danger','SRP_Note']
        labels={
            'SRP_LOG_Status':'Status',
            'SRP_LOG_User':'User',
            'SRP_LOG_Loss_of_Confidentiality':'Loss of Confidentiality',
            'SRP_LOG_Loss_of_Integrity':'Loss of Integrity',
            'SRP_LOG_Loss_of_Availability':'Loss of Availability',
            'SRP_LOG_Loss_of_Accountability':'Loss of Accountability',
            'SRP_LOG_Technical_Total':'Degree of Danger',
            'SRP_Note':'Note',
          
        }


class ReportBugForm(ModelForm):
    class Meta:
        model = Report_Bug
        fields =['Re_UserName','Re_Phone','Re_Email','Re_Title','Re_Description','Re_Report']
        labels={
            'Re_UserName':'Name',
            'Re_Phone':'Phone',
            'Re_Email':'Email',
            'Re_Title':'Title',
            'Re_Description':'Description',
            'Re_Report':'Report',

        }

    def __init__(self,*args,**kwargs):
        super(ReportBugForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class Admin_ReportBugForm(ModelForm):
    class Meta:
        model = Report_Bug
        fields =['Re_UserName','Re_Phone','Re_Email','Re_Title','Re_Description','Re_Report','Re_Status']
        exclude = ("Re_UserName","Re_Phone","Re_Email","Re_Title","Re_Description","Re_Report")        
        labels={

            'Re_Status':'Status',

        }

    def __init__(self,*args,**kwargs):
        super(Admin_ReportBugForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class ReBug_LOGSForm(ModelForm):
    class Meta:
        model = ReBug_LOGS
        fields =['ReBug_LOG_Status','ReBug_LOG_User']
        labels={
            'ReBug_LOG_Status':'Status',
            'ReBug_LOG_User':'User',
          
        }

class Admin_SRPForm_Status(ModelForm):
    class Meta:
        model = ServicesRequestParticipant
        fields =['SRP_Status']
        exclude = ("SRP_Status",)
    

    def __init__(self,*args,**kwargs):
        super(Admin_SRPForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
