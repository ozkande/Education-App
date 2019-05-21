from django.urls import path
from . import views

app_name = "introduction"

urlpatterns = [
    path('', views.tableofcontents, name = 'tableofcontents'),
    path('introduction', views.home, name = 'introduction-home'),
    path('tableofcontents', views.tableofcontents, name = 'table-of-contents'),
    path('contactus', views.contactus, name = 'contactus'),
    path('registration',views.registration, name='registration'),
    path('login', views.login_func, name ='login'),
    path('functions', views.functions, name = 'function'),
    path('exceptions', views.exceptions, name = 'exceptions'),
    path('decisionmaking', views.decisionmaking, name='decisionmaking'),
    path('agile', views.agile, name='agile'),
    path('scrum', views.scrum, name='scrum'),
    path('kanban', views.kanban, name='kanban'),
    path('docker', views.docker, name='docker'),
    path('gitcontrol', views.gitcontrol, name='gitcontrol'),
    path('cicd', views.cicd, name='cicd'),
    path('kubernetes', views.kubernetes, name='kubernetes'),


]