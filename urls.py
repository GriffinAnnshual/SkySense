from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('whatsapp/',views.whatsapp_permission,name='whatsapp_permission'),
    path('signup/',views.signup,name='signup'),
    path('smsdetails/',views.smsdetails,name='sms_details'),
    path('about/',views.about,name='about'),
    path('emergency/',views.emergency,name='emergency'),
    path('emergencynumbers/',views.emergency_numbers,name='emergency_numbers'),
    path('ajax/', views.handle_ajax_request, name='ajax'),
    path('officer_login/',views.officer_login,name='officer_login'),
    path('rescue_process/',views.rescue_process,name='rescue_process'),
    path('success/',views.success,name='success')
]
