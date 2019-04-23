from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:number>/', views.page, name='page'),
    path('result/<int:question_id>/', views.result, name='result'),
    path('q/<int:number>/', views.alternative, name='alternative')

]