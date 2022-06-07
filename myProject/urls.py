from django.contrib import admin
from django.urls import path, include
from gradesApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gradesApp/',include('gradesApp.urls')),
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('logout/',views.userLogout,name='logout'),
    path('studentDash/',views.studentDash,name='studentDash'),
    path('teacherDash/',views.teacherDash,name='teacherDash'),
    path('materials/', include('upload.urls')),
    path('post/', include('Post.urls')),
    path('assignment/', include('assignment.urls')),
    path('notice/', include('Notice.urls')),
    path('exam/', include('exam.urls')),
    path('zoom/', include('zoom.urls')),
    path('onlineExam/', include('onlineExam.urls')),
    path('chatbot/', include('chatbot.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
