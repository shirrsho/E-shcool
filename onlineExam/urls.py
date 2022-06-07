from django.urls import path
from onlineExam import views


app_name='onlineExam'

urlpatterns = [

    path('', views.FirstPage, name='firstPage'),
    path('faceDetection/', views.FaceRecognition, name='faceDetection'),
]
