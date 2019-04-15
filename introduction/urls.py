from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'introduction-home'),
    path('tableofcontents', views.tableofcontents, name = 'table-of-contents'),
    path('contactus', views.contactus, name = 'contactus'),
    path('registration',views.registration, name='registration'),
    path('login', views.login_func, name = 'login')

]