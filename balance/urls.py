from django.urls import path
from . import views

app_name = 'balance'

urlpatterns = [
    path('<int:question_id>/', views.index, name='index'),
    path('<int:question_id>/answer_click/', views.answer_click, name='answer_click'),
]