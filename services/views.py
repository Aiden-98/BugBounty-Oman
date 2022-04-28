from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,authenticate, logout
from .models import ServicesRequestParticipant, ServicesRequest, Awards, SR_LOGS, SRP_LOGS, ReBug_LOGS, Report_Bug
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Admin_CuProForm, addSRForm, SRPForm, AwardsForm, Admin_CyProForm, Admin_SRForm, Admin_SRPForm, Admin_SR_LOGS, Admin_SRP_LOGS, ReportBugForm, ReBug_LOGSForm, Admin_ReportBugForm, Admin_Cus_LOGS, Admin_Cy_LOGS, Admin_SRPForm_Status
from users.models import customerProfile,cyProfile, Cus_LOGS, Cy_LOGS

# Create your views here.
@login_required(login_url="cylogin")
def Service_Requests(request):

    if request.user.last_name != 'cy':
        return redirect('index')
    
    SRQ= ServicesRequest.objects.all()
    SRP=ServicesRequestParticipant.objects.all()
    val=1
    context ={'SRQ':SRQ, 'SRP':SRP, 'val':val}
    return render(request, 'Service_Requests.html',context)



@login_required(login_url="cylogin")
def single(request, pk):

    if request.user.last_name != 'cy' and request.user.last_name != 'org':
        return redirect('index')


    obj= ServicesRequest.objects.get(SR_ID=pk)
    obj_SRP= ServicesRequestParticipant.objects.filter(SR_ID=obj.SR_ID)
    srp_logs=Admin_SRP_LOGS()

    form =SRPForm()
    page="cy"

    if request.method =='POST':
        form = SRPForm(request.POST, request.FILES)
        srp_logs=Admin_SRP_LOGS(request.POST)
        if form.is_valid():
            form = form.save(commit=False)

            srp_logs = srp_logs.save(commit=False)

            form.CyRes_ID=request.user.cyprofile
            #hform.SR_ID=obj.SR_Organization_Name
            form.SR_ID=ServicesRequest.objects.get(SR_ID=pk)


            LOCon=form.SRP_Loss_of_Confidentiality
            LOIntg=form.SRP_Loss_of_Integrity
            LOAva=form.SRP_Loss_of_Availability
            LOAcc=form.SRP_Loss_of_Accountability

            con=1
            intg=1
            ava=1
            acc=1

            if LOCon == 'Low':
                con = 2
            elif LOCon == 'Medium':
                con = 4
            elif LOCon == 'High':
                con = 7
            elif LOCon == 'Critical':
                con = 9

            if LOIntg == 'Low':
                intg = 2
            elif LOIntg == 'Medium':
                intg = 4
            elif LOIntg == 'High':
                intg = 7
            elif LOIntg == 'Critical':
                intg = 9

            if LOAva == 'Low':
                ava = 2
            elif LOAva == 'Medium':
                ava = 4
            elif LOAva == 'High':
                ava = 7
            elif LOAva == 'Critical':
                ava = 9

            if LOAcc == 'Low':
                acc = 2
            elif LOAcc == 'Medium':
                acc = 4
            elif LOAcc == 'High':
                acc = 7
            elif LOAcc == 'Critical':
                acc = 9

            tot=(con + intg + ava + acc) / 4
            danger=" "

            if tot < 3 :
                danger="Low"
            elif tot >= 3 and tot < 6:
                danger ="Medium"
            elif tot >=6 and tot < 8:
                danger="High"
            else:
                danger="Critical"

                       


            form.SRP_Total = tot
            form.SRP_Danger = danger

            form.save()

            srp_logs.SRP_LOG_Status=form.SRP_Status
            srp_logs.SRP_ID=form
            srp_logs.SRP_LOG_User=request.user.username

            srp_logs.SRP_LOG_Loss_of_Confidentiality = form.SRP_Loss_of_Confidentiality
            srp_logs.SRP_LOG_Loss_of_Integrity = form.SRP_Loss_of_Integrity
            srp_logs.SRP_LOG_Loss_of_Availability =form.SRP_Loss_of_Availability
            srp_logs.SRP_LOG_Loss_of_Accountability =form.SRP_Loss_of_Accountability
            #srp_logs.SRP_LOG_Technical_Total = form.SRP_Total
            srp_logs.SRP_LOG_Technical_Total = tot
            srp_logs.SRP_LOG_Danger = danger

            srp_logs.save()
            
            
            messages.success(request,'Report submitted successfully')

            return redirect('index')
        
        else:
            messages.error(request,'An error happend!')

    val=0
    context ={'obj':obj,'form':form, 'page':page, 'obj_SRP':obj_SRP, 'val':val}
    return render(request, 'Single_Request.html',context)






@login_required(login_url="cylogin")
def Add_Service_Requests(request):


    if request.user.last_name != 'org':
        return redirect('index')
    
    page = '1'
    form =addSRForm(request.POST, request.FILES)

    if request.method =='POST':
        form = addSRForm(request.POST, request.FILES)
        if form.is_valid():
            hform = form.save(commit=False)
            hform.SR_Organization_Name=request.user.customerprofile.CuRes_Org_Name
            hform.CuRes_ID=request.user.customerprofile

            package= ""
            if request.POST['select'] == "1":
                package= "Basic Package"
            elif request.POST['select'] == "2":
                package= "Advance Package"
            else:
                package= "Legand Package"

            hform.SR_Package=package

            hform.save()
            
            messages.success(request,'Request created successfully')

            return redirect('cuRequests')
        
        else:
            messages.error(request,'An error happend!')



    context={'page':page,'form':form}



    return render(request, 'Add_Service_Requests.html', context)

@login_required(login_url="cylogin")
def payment(request, pk):
    # page = '1'
    # form =addSRForm()

    # if request.method =='POST':
    #     form = addSRForm(request.POST)
    #     if form.is_valid():
    #         hform = form.save(commit=False)
    #         hform.CuRes_ID=request.user.customerprofile
    #         hform.save()
            
    #         messages.success(request,'User account created')

    #         return redirect('profile')
        
    #     else:
    #         messages.error(request,'An error happend!')



    # context={'page':page,'form':form}



    return render(request, 'payment.html')



@login_required(login_url="cylogin")
def customerRequests(request):

    if request.user.last_name != 'org':
        return redirect('index')


    SRQ= ServicesRequest.objects.all().order_by('-SR_Created')
    context ={'SRQ':SRQ}
    return render(request, 'customer_requests.html',context)

@login_required(login_url="cylogin")
def AddAward(request, pk):

    
    if request.user.last_name != 'admin':
        return redirect('index')

    obj= ServicesRequestParticipant.objects.get(SRP_ID=pk)
    form =AwardsForm()
    page="cy"

    if request.method =='POST':
        form = AwardsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            #hform.SR_ID=obj.SR_Organization_Name
            form.SRP_ID=ServicesRequestParticipant.objects.get(SRP_ID=pk)
            form.SRA_User_Created=request.user.username
            form.SRA_Danger_Of_Vuln=obj.SRP_Total
            
            prize=""
            if obj.SRP_Danger == 'Low':
                prize=obj.SR_ID.SR_Low_Award
            elif obj.SRP_Danger == 'Medium':
                prize=obj.SR_ID.SR_Medium_Award
            elif obj.SRP_Danger == 'High':
                prize=obj.SR_ID.SR_High_Award
            elif obj.SRP_Danger == 'Critical':
                prize=obj.SR_ID.SR_Critical_Award
            else:
                prize=0
            
            form.SRA_prize=prize
            obj.SRP_Status="Ended"

            form.save()
            obj.save()

            
            
            messages.success(request,'Award added successfully')

            return redirect('adminp')
        
        else:
            messages.error(request,'An error happend!')

    context ={'obj':obj,'form':form, 'page':page}
    return render(request, 'Add_Award.html',context)


@login_required(login_url="cylogin")
def AdminCy(request, pk):

    if request.user.last_name != 'admin':
        return redirect('index')

    obj= cyProfile.objects.get(CyRes_ID=pk)
    form =Admin_CyProForm(instance=obj)
    Cy_Logs=Admin_Cy_LOGS()
    Cy_Logs_obj=Cy_LOGS.objects.filter(CyRes_ID=pk).order_by('-Cy_Created')

    page="cy"

    if request.method =='POST':
        form = Admin_CyProForm(request.POST, request.FILES,  instance=obj)
        Cy_Logs=Admin_Cy_LOGS(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            Cy_Logs = Cy_Logs.save(commit=False)
            #form.CyRes_ID=cyProfile.objects.get(CyRes_ID=pk)

            Cy_Logs.CyRes_ID=form
            Cy_Logs.Cy_LOG_Status=form.CuRes_Status
            Cy_Logs.Cy_LOG_Sector=form.CyRes_Service_Type
            Cy_Logs.Cy_LOG_Note=form.CyRes_Note
            Cy_Logs.Cy_LOG_User=request.user.username

            form.save()
            Cy_Logs.save()

            
            messages.success(request,'cyber Researcher Changed successfully')

            return redirect('adminp')
        
        else:
            messages.error(request,'An error happend!')

    context ={'obj':obj,'form':form, 'page':page, 'Cy_Logs_obj':Cy_Logs_obj}
    return render(request, 'admin/admin_cyPro.html',context)


@login_required(login_url="cylogin")
def AdminCu(request, pk):

    if request.user.last_name != 'admin':
        return redirect('index')

    obj= customerProfile.objects.get(CuRes_ID=pk)
    form =Admin_CuProForm(instance=obj)
    Cus_Logs=Admin_Cus_LOGS()
    Cus_Logs_obj=Cus_LOGS.objects.filter(CuRes_ID=pk).order_by('-Cus_Created')

    page="org"

    if request.method =='POST':
        form = Admin_CuProForm(request.POST, request.FILES,  instance=obj)
        Cus_Logs=Admin_Cus_LOGS(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            Cus_Logs = Cus_Logs.save(commit=False)

           #form.CyRes_ID=cyProfile.objects.get(CyRes_ID=pk)
            Cus_Logs.CuRes_ID=form
            Cus_Logs.Cus_LOG_Status=form.CuRes_Status
            Cus_Logs.Cus_LOG_Sector=form.CuRes_organization_Sector
            Cus_Logs.Cus_LOG_Note=form.CuRes_Note
            Cus_Logs.Cus_LOG_User=request.user.username


            form.save()
            Cus_Logs.save()

            messages.success(request,'Customer Changed successfully')

            return redirect('adminp')
        
        else:
            messages.error(request,'An error happend!')

    context ={'obj':obj,'form':form, 'page':page, 'Cus_Logs_obj':Cus_Logs_obj}
    return render(request, 'admin/admin_CuPro.html',context)


@login_required(login_url="cylogin")
def AdminSR(request, pk):

    
    if request.user.last_name != 'admin':
        return redirect('index')

    obj= ServicesRequest.objects.get(SR_ID=pk)
    form =Admin_SRForm(instance=obj)
    sr_logs=Admin_SR_LOGS()
    SrLogs=SR_LOGS.objects.filter(SR_ID=pk).order_by('-SRA_Created')

    page="cy"

    if request.method =='POST':
        form = Admin_SRForm(request.POST, request.FILES,  instance=obj)
        sr_logs=Admin_SR_LOGS(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            sr_logs = sr_logs.save(commit=False)

            #form.CyRes_ID=cyProfile.objects.get(CyRes_ID=pk)
            sr_logs.SR_LOG_Status=form.SR_Approval_status
            sr_logs.SR_ID=form
            sr_logs.SR_LOG_User=request.user.username

            sr_logs.save()
            form.save()
            
            messages.success(request,'Service Request')

            return redirect('adminp')
        
        else:
            messages.error(request,'An error happend!')

    context ={'obj':obj,'form':form, 'page':page, 'sr_logs':sr_logs, 'SrLogs':SrLogs}
    return render(request, 'admin/admin_change.html',context)


@login_required(login_url="cylogin")
def AdminSRP(request, pk):

    
    if request.user.last_name != 'admin':
        return redirect('index')

    obj= ServicesRequestParticipant.objects.get(SRP_ID=pk)
    form =Admin_SRPForm(instance=obj)
    srp_logs=Admin_SRP_LOGS()
    SrpLogs=SRP_LOGS.objects.filter(SRP_ID=pk).order_by('-SRP_Created')

    page="cy"

    if request.method =='POST':
        form = Admin_SRPForm(request.POST, request.FILES,  instance=obj)
        srp_logs=Admin_SRP_LOGS(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            srp_logs = srp_logs.save(commit=False)

            #form.CyRes_ID=cyProfile.objects.get(CyRes_ID=pk)

            srp_logs.SRP_LOG_Status=form.SRP_Status
            srp_logs.SRP_ID=form
            srp_logs.SRP_LOG_User=request.user.username
            srp_logs.SRP_Note=form.SRP_Note

            srp_logs.SRP_LOG_Loss_of_Confidentiality = form.SRP_Loss_of_Confidentiality
            srp_logs.SRP_LOG_Loss_of_Integrity = form.SRP_Loss_of_Integrity
            srp_logs.SRP_LOG_Loss_of_Availability =form.SRP_Loss_of_Availability
            srp_logs.SRP_LOG_Loss_of_Accountability =form.SRP_Loss_of_Accountability

            LOCon=form.SRP_Loss_of_Confidentiality
            LOIntg=form.SRP_Loss_of_Integrity
            LOAva=form.SRP_Loss_of_Availability
            LOAcc=form.SRP_Loss_of_Accountability

            con=1
            intg=1
            ava=1
            acc=1

            if LOCon == 'Low':
                con = 2
            elif LOCon == 'Medium':
                con = 4
            elif LOCon == 'High':
                con = 7
            elif LOCon == 'Critical':
                con = 9

            if LOIntg == 'Low':
                intg = 2
            elif LOIntg == 'Medium':
                intg = 4
            elif LOIntg == 'High':
                intg = 7
            elif LOIntg == 'Critical':
                intg = 9

            if LOAva == 'Low':
                ava = 2
            elif LOAva == 'Medium':
                ava = 4
            elif LOAva == 'High':
                ava = 7
            elif LOAva == 'Critical':
                ava = 9

            if LOAcc == 'Low':
                acc = 2
            elif LOAcc == 'Medium':
                acc = 4
            elif LOAcc == 'High':
                acc = 7
            elif LOAcc == 'Critical':
                acc = 9

            tot=(con + intg + ava + acc) / 4
            
            danger=" "
            
            if tot < 3 :
                danger="Low"
            elif tot >= 3 and tot < 6:
                danger ="Medium"
            elif tot >=6 and tot < 8:
                danger="High"
            else:
                danger="Critical"

                       
            form.SRP_Danger = danger
            srp_logs.SRP_LOG_Danger = danger

            form.SRP_Technical_Total = tot
            srp_logs.SRP_LOG_Technical_Total = tot

            srp_logs.save()
            form.save()
            
            messages.success(request,'Services Request Participant Changed Successfully')

            return redirect('adminp')
        
        else:
            messages.error(request,'An error happend!')

    context ={'obj':obj,'form':form, 'page':page, 'srp_logs':srp_logs, 'SrpLogs':SrpLogs}
    return render(request, 'admin/admin_change_SRP.html',context)



def ReportBug(request):

    form=ReportBugForm(request.POST)


    if request.method =='POST':
        form=ReportBugForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            Re_UserName=" "
            Re_Cyb=""
            if request.user.is_authenticated:
                Re_UserName="User Name: ("+request.user.username + ") In Form name: " + request.POST['Re_UserName']
                if request.user.last_name == "cy":
                    Re_Cyb=request.user.cyprofile
                    form.CyRes_ID=Re_Cyb

            else:    
                Re_UserName = request.POST['Re_UserName'] + " (Not Registered)"

            Re_Phone = request.POST['Re_Phone']
            Re_Email = request.POST['Re_Email']
            Re_Title = request.POST['Re_Title']
            Re_Description = request.POST['Re_Description']
            Re_Report = request.POST['Re_Report']
 
                

            form.Re_UserName=Re_UserName
            form.Re_Phone=Re_Phone
            form.Re_Email=Re_Email
            form.Re_Title=Re_Title
            form.Re_Description=Re_Description
            form.Re_Report=Re_Report

            
            form.save()
            
            messages.success(request,'Report Submitted Successfully')

            return redirect('index')
        
        else:
            messages.error(request,'An error happend!')

    context ={'form':form}
    return render(request, 'report_bug.html',context)




@login_required(login_url="cylogin")
def AdminReBUg(request, pk):

    
    if request.user.last_name != 'admin':
        return redirect('index')

    obj= Report_Bug.objects.get(Re_ID=pk)
    form =Admin_ReportBugForm(instance=obj)
    Re_log=ReBug_LOGSForm()
    Relogs=ReBug_LOGS.objects.filter(Re_ID=pk).order_by('-ReBug_Created')


 
    if request.method =='POST':
        form = Admin_ReportBugForm(request.POST, request.FILES,  instance=obj)
        Re_log=ReBug_LOGS(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            Re_log.ReBug_LOG_Status=form.Re_Status
            Re_log.Re_ID=form
            Re_log.ReBug_LOG_User=request.user.username

            Re_log.save()
            form.save()
            
            messages.success(request,'Report Updated Successfully')

            return redirect('adminp')
        
        else:
            messages.error(request,'An error happend!')

    context ={'obj':obj,'form':form, 'Re_log':Re_log, 'Relogs':Relogs}
    return render(request, 'admin/admin_change_ReportBug.html',context)
