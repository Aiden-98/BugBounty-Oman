from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    #path('',views.index,name='index'),
    path('edit-profile',views.cyProfiles,name='profile'),
    path('profile', views.uProfile, name='uprofile'),
    path('logout',views.logoutUser,name='logout'),
    path('Login',views.CyLog,name='cylogin'),
    path('Registration',views.CyReg,name='cyReg'),
    path('',views.index,name='index'),
    path('admin-panel',views.adminp,name='adminp'),
    path('logout-screen',views.logout_screen,name='logout_screen'),
    path('admin-single/<str:pk>/',views.Admin_single,name='single_admin'),
    path('admin-single-SRP/<str:pk>/',views.Admin_single_SRP,name='single_SRP_admin'),
    path('Submitted-Report',views.Cy_Submitted_Report,name='SubmittedReport'),
    path('Cyber-Report/<str:pk>/',views.Cy_single,name='Cy_single'),




]