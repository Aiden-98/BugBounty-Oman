from django.db.models import fields
from django.forms import ModelForm, widgets
from django import forms
from .models import customerProfile,cyProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CyProForm(ModelForm):
    class Meta:
        model = cyProfile
        fields =['CyRes_UserName','CyRes_Name','CyRes_Email','CyRes_Phone','CyRes_Bio','CyRes_Profile_Image','CyRes_Service_Type','CyRes_Documents']
        exclude = ("CyRes_Service_Type",)

        labels={
            'CyRes_UserName':'Userame',
            'CyRes_Name':'Name',
            'CyRes_Email':'Email',
            'CyRes_Phone':'Phone',
            'CyRes_Bio':'Bio',
            'CyRes_Profile_Image':'Profile Picture',
            'CyRes_Service_Type':'Type',
            'CyRes_Documents':'Documents'
        }

    def __init__(self,*args,**kwargs):
        super(CyProForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        



class CuProForm(ModelForm):
    class Meta:
        model = customerProfile
        fields =['CuRes_Org_Name','CuRes_Contact_Person','CuRes_Contact_Designation','CuRes_Email','CuRes_Phone','CuRes_Profile_Image','CuRes_Description','CuRes_organization_Sector', 'CuRes_Documents']
        exclude = ("CuRes_organization_Sector","CuRes_Org_Name",)

        labels={
            'CuRes_Contact_Person':'Company Name',
            'CuRes_Contact_Designation':'Contact Designation',
            'CuRes_Email':'Email',
            'CuRes_Phone':'Phone',
            'CuRes_Profile_Image':'Profile Picture',
            'CuRes_Description':'About Organization',
            'CuRes_organization_Sector':'Organization Type',
            'CuRes_Documents':'Documents'
            
        }


    def __init__(self,*args,**kwargs):
        super(CuProForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        



class CustomSelect(forms.Select):
    option_inherits_attrs = True

Types = [
    ('cy', 'Cyber Researcher'),
    ('org', 'Organization'),
    ]

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =['first_name','last_name','email','username','password1','password2']
        labels={
            'first_name':'Name / Organization Name',
            'last_name':'Type'
        }
        #fields ='__all__'
        widgets={
            'last_name':forms.Select(choices=Types),
        }
        

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})





