from django.urls import path
from assignment import views
from assignment.views import AssignmentDetailView, AEvaluationDetailView, SolutionDetailView


app_name='assignment'

urlpatterns = [

    path('', views.assignment_list, name='assignment_list'),
    path('upload_assignment/', views.upload_assignment, name='upload_assignment'),
    path('assignment/<int:pk>/', AssignmentDetailView.as_view(), name='assignment_detail'),
    path('evaluation/', views.assignment_evaluation_list, name='a_evaluation_list'),
    path('evaluation/<int:pk>', AEvaluationDetailView.as_view(), name='a_solution_list'),
    path('evaluation/detail/<int:pk>', SolutionDetailView.as_view(), name='a_solution_detail'),

]
