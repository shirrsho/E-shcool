from django.urls import path
from Notice import views
from .views import NoticeDetail


app_name='Notice'

urlpatterns = [

    path('', views.notice_list, name='notice_list'),
    path('<int:pk>/', NoticeDetail.as_view(), name='notice_detail'),
]
