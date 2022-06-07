from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import AssignmentForm, SolutionForm
from .models import Assignment, Solution
from django.views import View
from django.urls import reverse_lazy

# Create your views here.


def assignment_list(request):
    assignments = Assignment.objects.all().order_by('-due')
    return render(request, 'assignment/assignment_list.html', {
        'assignments': assignments
    })

def upload_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            new_assignment = form.save(commit=False)
            new_assignment.author = request.user
            new_assignment.save()

    else:
        form = AssignmentForm()
    return render(request, 'assignment/upload_assignment.html', {
        'form': form
    })


class AssignmentDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        problem = Assignment.objects.get(pk=pk)
        form = SolutionForm()


        context = {
            'problem': problem,
            'form': form,
        }

        return render(request, 'assignment/assignment_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        print(request.POST)
        problem = Assignment.objects.get(pk=pk)
        form = SolutionForm(request.POST)

        if form.is_valid():
            print('xyz')
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.problem = problem
            new_comment.save()


        context = {
            'problem': problem,
            'form': form,
        }

        return render(request, 'assignment/assignment_detail.html', context)


def assignment_evaluation_list(request):
    assignments = Assignment.objects.all().order_by('-due')
    return render(request, 'assignment/a_evaluation_list.html', {
        'assignments': assignments
    })


class AEvaluationDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        prob = Assignment.objects.get(pk=pk)

        solution = Solution.objects.filter(problem=prob).order_by('-submission_time')

        context = {
            'problem': prob,
            'solution': solution,
        }

        return render(request, 'assignment/a_solution_list.html', context)


class SolutionDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        solution = Solution.objects.get(pk=pk)

        context = {
            'solution': solution,
        }

        return render(request, 'assignment/a_solution_detail.html', context)
