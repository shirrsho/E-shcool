from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import ExamForm, ExamSolutionForm
from .models import Exam, ExamSolution
from django.views import View
from django.urls import reverse_lazy

import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
# Create your views here.


def exam_list(request):
    assignments = Exam.objects.all().order_by('-due')
    return render(request, 'exam/exam_list.html', {
        'assignments': assignments
    })

def upload_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            new_assignment = form.save(commit=False)
            new_assignment.author = request.user
            new_assignment.save()

    else:
        form = ExamForm()
    return render(request, 'exam/upload_exam.html', {
        'form': form
    })


class ExamDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        problem = Exam.objects.get(pk=pk)
        form = ExamSolutionForm()


        context = {
            'problem': problem,
            'form': form,
        }

        return render(request, 'exam/exam_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        print(request.POST)
        problem = Exam.objects.get(pk=pk)
        form = ExamSolutionForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.problem = problem
            new_comment.save()


        context = {
            'problem': problem,
            'form': form,
        }

        return render(request, 'exam/exam_detail.html', context)



def exam_evaluation_list(request):
    assignments = Exam.objects.all().order_by('-due')
    return render(request, 'exam/evaluation_list.html', {
        'assignments': assignments
    })



class EvaluationDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        prob = Exam.objects.get(pk=pk)

        solution = ExamSolution.objects.filter(problem=prob).order_by('-submission_time')

        context = {
            'problem': prob,
            'solution': solution,
        }

        return render(request, 'exam/solution_list.html', context)


class SolutionDetailView(View):
    def get(self, request, pk, *args, **kwargs):

        significance_level = 1.26
        solution = ExamSolution.objects.get(pk=pk)

        sampleSol = solution.problem.sampleSolution


        X = solution.answer
        Y = sampleSol

        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        # Using loop + punctuation string
        for ele in X:
            if ele in punc:
                X = X.replace(ele, "")


        for ele in Y:
            if ele in punc:
                Y = Y.replace(ele, "")


        X_list = word_tokenize(X)
        Y_list = word_tokenize(Y)

        sw = stopwords.words('english')

        l1 =[]
        l2 =[]

        # remove stop words from the string
        X_set = {w for w in X_list if not w in sw}
        Y_set = {w for w in Y_list if not w in sw}

        rvector = X_set.union(Y_set)
        # print(rvector)

        for w in rvector:

            synonyms = []

            for syn in wordnet.synsets(w):
	               for l in syn.lemmas():
		                 synonyms.append(l.name())


            for s in range(len(synonyms)):
                if synonyms[s] in X_set:
                    l1.append(1)
                    break
                else:
                    if s+1 == len(synonyms):
                        l1.append(0)

            for s in range(len(synonyms)):
                if synonyms[s] in Y_set:
                    l2.append(1)
                    break
                else:
                    if s+1 == len(synonyms):
                        l2.append(0)

        c=0

        for i in range(len(rvector)):
            c+= l1[i]*l2[i]

        cosine = c / float((sum(l1)*sum(l2))**0.5)
        cosine = cosine*significance_level*100


        context = {
            'solution': solution,
            'sampleSol': sampleSol,
            'result': cosine
        }

        return render(request, 'exam/solution_detail.html', context)



def Algorithm_detail(request):
    return render(request, 'exam/algorithm_detail.html', context={})
