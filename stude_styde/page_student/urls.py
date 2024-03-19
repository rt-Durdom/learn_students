from django.urls import path

from . import views

app_name = 'page_student'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='post_form'),
]