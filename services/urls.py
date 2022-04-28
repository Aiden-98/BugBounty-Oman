from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    #path('',views.cyProfiles,name='cyProfiles'),
    path('',views.Service_Requests,name='SR_Request'),
    path('Add',views.Add_Service_Requests,name='addSR'),
    path('single/<str:pk>/', views.single, name='singleSR'),
    path('request-details/<str:pk>/', views.single, name='singleDe'),
    path('payment/<str:pk>/', views.payment, name='payment'),
    path('requests', views.customerRequests, name='cuRequests'),
    path('add-award/<str:pk>/',views.AddAward,name='addawd'),
    path('change-cy/<str:pk>/',views.AdminCy,name='admincy'),
    path('change-cu/<str:pk>/',views.AdminCu,name='admincu'),
    path('change-sr/<str:pk>/',views.AdminSR,name="adminsr"),
    path('change-srp/<str:pk>/',views.AdminSRP,name="adminsrp"),
    path('report-bug', views.ReportBug, name='reportbug'),
    path('change-Report-Bug/<str:pk>/',views.AdminReBUg,name="changeReBug"),

]