from django.urls import path
from zoom import views


app_name='zoom'

urlpatterns = [

    path('', views.createForm, name='create_meeting'),
    path('form_list/', views.zoom_list, name='form_list'),

]
