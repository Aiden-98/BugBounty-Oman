from django.http import HttpResponseRedirect
from django.contrib.auth import forms
from django.template.loader import render_to_string
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
from .models import cyProfile,customerProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CyProForm, CustomUserCreationForm, CuProForm
from services.forms import SRPForm
from services.models import Awards, ServicesRequest, ServicesRequestParticipant, Report_Bug
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

@login_required(login_url='cylogin')
def cyProfiles(request):
    cur_user=request.user.last_name
    print(cur_user)
    if str(cur_user) == 'cy':

        profile=request.user.cyprofile
        form=CyProForm(instance=profile)

        if request.method == 'POST':
            form=CyProForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()

                return redirect('uprofile')
    
    else:

        profile=request.user.customerprofile
        form=CuProForm(instance=profile)

        if request.method == 'POST':
            form=CuProForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()

                return redirect('uprofile')

    context={'form':form, 'cur_user':cur_user}

    return render(request, 'editProfiles.html', context)



@login_required(login_url='cylogin')
def uProfile(request):
    cur_user=request.user.last_name
    AwardsForms=Awards.objects.all()

    print(cur_user)
    if str(cur_user) == 'cy':

        profile=request.user.cyprofile
        form=CyProForm(instance=profile)

        if request.method == 'POST':
            form=CyProForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()

                return redirect('index')
    
    else:

        profile=request.user.customerprofile
        form=CuProForm(instance=profile)

        if request.method == 'POST':
            form=CuProForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()

                return redirect('index')

    if request.user.last_name == 'cy':
        SRP_form=ServicesRequestParticipant.objects.filter(CyRes_ID=request.user.cyprofile.CyRes_ID)
    else:
        SRP_form=" "

    SRP_Low=0
    SRP_Medium=0
    SRP_High=0
    SRP_Critical=0

    if request.user.last_name == 'cy':

        for SRP in SRP_form:
            if SRP.SRP_Status == "Ended":

                if SRP.SRP_Danger == "Low":
                    SRP_Low+=1
    
                if SRP.SRP_Danger == "Medium":
                    SRP_Medium+=1

                if SRP.SRP_Danger == "High":
                    SRP_High+=1

                if SRP.SRP_Danger == "Critical":
                    SRP_Critical+=1

    context={'form':form, 'cur_user':cur_user, 'awards':AwardsForms, 'SRP_Low':SRP_Low,'SRP_form':SRP_form, 'SRP_Medium':SRP_Medium, 'SRP_High':SRP_High, 'SRP_Critical':SRP_Critical}

    return render(request, 'userProfile.html', context)




def index(request):

    if request.method == 'POST':
        name = request.POST['name'] +" "
        email = request.POST['email'] +" "   
        subject = request.POST['subject'] +" "    
        message = request.POST['message'] + " "   

        send_mail(
            subject,
            "Sender name:"+name+"\nSender Email: "+email+"\n\n"+"Message:\n"+message,
            email,
            ['', email], #add your email in the empty field [abc@gmail.com for example]
            fail_silently=False,
            )                


    return render(request, 'index.html')


def CyLog(request):
    page = 'login'
    context={'page':page}


    if request.user.is_authenticated:
        return redirect('index')


    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username Does not exist')
        
        user=authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'Username or password is inccorect')

    return render(request, 'Register_login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request,'User Logged out')
    return redirect('logout_screen')


def CyReg(request):
    page = 'register'
    form =CustomUserCreationForm()

    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,'User account created')

            login(request,user)
            return redirect('profile')
        
        else:
            messages.error(request,'An error happend!')



    context={'page':page,'form':form}

    return render(request, 'Register_login.html', context)


def CyCu(request):
    return render(request, 'index.html')


def adminp(request):

    if request.user.last_name != 'admin':
        return redirect('index')


    form_org=customerProfile.objects.all().order_by('-CuRes_Created')
    form_cy=cyProfile.objects.all()
    form_SR=ServicesRequest.objects.all().order_by('-SR_Created')
    form_SRP=ServicesRequestParticipant.objects.all().order_by('-SRP_Created')
    form_Awd=Awards.objects.all().order_by('-SRA_Created')
    form_org_sr=ServicesRequest.objects.values_list('CuRes_ID', flat=True).distinct()
    form_org_srp=ServicesRequestParticipant.objects.values_list('SR_ID', flat=True).distinct()
    form_ReBug=Report_Bug.objects.all()

    context={
        'form_org':form_org,
        'form_cy':form_cy,
        'form_SR':form_SR,
        'form_SRP':form_SRP,
        'form_Awd':form_Awd,
        'form_org_sr':form_org_sr,
        'form_org_srp':form_org_srp,
        'form_ReBug':form_ReBug,


    }

    return render(request, 'adminPanel.html',context)


def logout_screen(request):

    return render(request, 'logout.html')


@login_required(login_url="cylogin")
def Admin_single(request, pk):

    if request.user.last_name != 'admin':
        return redirect('index')

    form_org=customerProfile.objects.get(CuRes_ID=pk)
    form_cy=cyProfile.objects.all()
    form_SR=ServicesRequest.objects.all().order_by('-SR_Created')
    form_SRP=ServicesRequestParticipant.objects.all().order_by('-SRP_Created')
    form_Awd=Awards.objects.all().order_by('-SRA_Created')

   

    context={
        'form_org':form_org,
        'form_cy':form_cy,
        'form_SR':form_SR,
        'form_SRP':form_SRP,
        'form_Awd':form_Awd,
        
    }
    return render(request, 'admin_single.html',context)



@login_required(login_url="cylogin")
def Admin_single_SRP(request, pk):

    if request.user.last_name != 'admin':
        return redirect('index')

    form_org=customerProfile.objects.all()
    form_cy=cyProfile.objects.all()
    form_SR=ServicesRequest.objects.get(SR_ID=pk)
    form_SRP=ServicesRequestParticipant.objects.all().order_by('-SRP_Created')
    form_Awd=Awards.objects.all().order_by('-SRA_Created')

   

    context={
        'form_org':form_org,
        'form_cy':form_cy,
        'form_SR':form_SR,
        'form_SRP':form_SRP,
        'form_Awd':form_Awd,
        
    }
    return render(request, 'admin_single-SRP.html',context)


@login_required(login_url="cylogin")
def Cy_Submitted_Report(request):

    if request.user.last_name != 'cy':
        return redirect('index')

    SRP= ServicesRequestParticipant.objects.all().order_by('-SRP_Created')
    context ={'SRP':SRP}
    return render(request, 'Cy_submitted_Reports.html',context)


@login_required(login_url="cylogin")
def customerRequests(request):

    if request.user.last_name != 'admin':
        return redirect('index')

    SRQ= ServicesRequest.objects.all().order_by('-SR_Created')
    context ={'SRQ':SRQ}
    return render(request, 'customer_requests.html',context)



@login_required(login_url="cylogin")
def Cy_single(request, pk):

    if request.user.last_name != 'cy' and request.user.last_name != 'org':
        return redirect('index')

    obj= ServicesRequestParticipant.objects.get(SRP_ID=pk)

    form =SRPForm()
    page="cy"

    val=0
    context ={'obj':obj,'form':form,  'val':val}
    return render(request, 'Cy_Single_Report.html',context)


# @login_required(login_url="cylogin")
# def MainPage(request, pk):

#     send_mail(
#         'Test1',
#         'Message.',
#         settings.EMAIL_HOST_USER,
#         [profile.CyRes_Email],
#         fail_silently=False,

#             )
#     return render(request, 'index.html',context)
