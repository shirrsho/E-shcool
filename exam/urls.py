from django.urls import path
from exam import views
from exam.views import ExamDetailView, EvaluationDetailView, SolutionDetailView


app_name='exam'

urlpatterns = [

    path('', views.exam_list, name='exam_list'),
    path('upload_exam/', views.upload_exam, name='upload_exam'),
    path('evaluation/', views.exam_evaluation_list, name='evaluation_list'),
    path('<int:pk>/', ExamDetailView.as_view(), name='exam_detail'),
    path('evaluation/<int:pk>/', EvaluationDetailView.as_view(), name='solution_list'),
    path('evaluation/detail/<int:pk>', SolutionDetailView.as_view(), name='solution_detail'),
    path('evaluation/detail/algorithm', views.Algorithm_detail, name='algorithm_detail'),

]
