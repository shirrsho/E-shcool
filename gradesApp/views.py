from django.shortcuts import render,redirect
from gradesApp.forms import studentForm,studentAddForm,teacherForm,teacherAddForm,EditProfile
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from gradesApp.models import Student,Teacher,UserProfile
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'gradesApp/index.html')

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    return render(request,'gradesApp/register.html')

def registerStudent(request):
    registered=False
    if request.method=='POST':
        var_studentForm=studentForm(request.POST)
        var_studentAddForm=studentAddForm(request.POST)
        if var_studentForm.is_valid() and var_studentAddForm.is_valid():
            studentprimary=var_studentForm.save()
            studentprimary.set_password(studentprimary.password)
            studentprimary.save()
            studentAdd=var_studentAddForm.save(commit=False)
            studentAdd.student=studentprimary
            studentAdd.save()
            registered=True
    else:
        var_studentForm=studentForm()
        var_studentAddForm=studentAddForm()
    return render(request,'gradesApp/registerStudent.html',{'var_studentForm':var_studentForm,'var_studentAddForm':var_studentAddForm,'registered':registered})


def registerTeacher(request):
    registered=False
    if request.method=='POST':
        var_teacherForm=teacherForm(request.POST)
        var_teacherAddForm=teacherAddForm(request.POST)
        if var_teacherForm.is_valid() and var_teacherAddForm.is_valid():
            teacherprimary=var_teacherForm.save()
            teacherprimary.set_password(teacherprimary.password)
            teacherprimary.save()
            teacherAdd=var_teacherAddForm.save(commit=False)
            teacherAdd.teacher=teacherprimary
            teacherAdd.save()
            registered=True
    else:
        var_teacherForm=teacherForm()
        var_teacherAddForm=teacherAddForm()
    return render(request,'gradesApp/registerTeacher.html',{'var_teacherForm':var_teacherForm,'var_teacherAddForm':var_teacherAddForm,'registered':registered})

def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/gradesApp/coursePage')
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('/gradesApp/login/')
    else:
        return render(request,'gradesApp/login.html',{'invalidlogin':invalidlogin})

@login_required
def dashboard(request):
    try:
        current=Student.objects.get(student=request.user)
    except Student.DoesNotExist:
        current=Teacher.objects.get(teacher=request.user)
    if current.is_student:
        return redirect('/studentDash/')
    else:
        return redirect('/teacherDash/')
    return render(request,'gradesApp/dashboard.html')



def studentDash(request):
    return render(request,'gradesApp/courseList.html')

def teacherDash(request):
    return render(request,'gradesApp/courseList.html')


@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)


    return render(request, 'gradesApp/profile.html', context={'form':form})


@login_required
def viewProfile(request):
    current_user = UserProfile.objects.get(user=request.user)

    context = {
        'profile': current_user
    }

    return render(request, 'gradesApp/viewProfile.html', context)


@login_required
def CoursePage(request):

    courseList = []
    courseCode = []

    try:
        current=Student.objects.get(student=request.user)
    except Student.DoesNotExist:
        current=Teacher.objects.get(teacher=request.user)
    if current.is_student:
        semester = current.semester
        if semester=='1':
            courseList = ['Structured Programming', 'Discrete Mathematics', 'Probability & Statistics', 'Sociology', 'Introduction to Software Engineering', 'Calculus & Analytical Geometry']
            courseCode = ['CSE 101', 'CSE 102', 'STAT 103', 'MATH 104', 'GE 105', 'SE 106']
        elif semester=='2':
            courseList = ['Data Structure and Algorithm', 'Computer Organization', 'Probability and Statistics for Engineers II', 'Ordinary Differential Equations', 'Bangladesh Studies', 'Object Oriented Concepts I']
            courseCode = ['CSE 201', 'CSE 211', 'STAT 203', 'MATH 204', 'GE 212', 'SE 206']
        elif semester=='3':
            courseList = ['Combinatorial Optimization', 'Theory of Computing', 'Computer Networking', 'Numerical Analysis for Engineers', 'Software Project Lab I', 'Object Oriented Concepts II']
            courseCode = ['CSE 301', 'SE 312', 'CSE 311', 'MATH 304', 'SE 305', 'SE 306']
        elif semester=='4':
            courseList = ['Operating System and System Programming', 'Business Psychology', 'Information Security', 'Database Management System I', 'Business Studies for Engineers ', 'Software Requirements Specification and Analysis']
            courseCode = ['CSE 401', 'GE 402', 'CSE 411', 'CSE 404', 'BUS 405', 'SE 406']
        elif semester=='5':
            courseList = ['Professional Ethics for Information Systems', 'Web Technology', 'Business Communications', 'Database Management System II', 'Software Project Lab II', 'Design Patterns']
            courseCode = ['SE5 11', 'CSE 502', 'BUS 503', 'CSE 504', 'SE 505', 'SE 506']
        elif semester=='6':
            courseList = ['Distributed Systems', 'Software Metrics', 'Software Security', 'Artificial Intelligence', 'Software Testing and Quality Assurance', 'Software Design and Analysis']
            courseCode = ['CSE 601', 'SE 611', 'SE 612', 'CSE 604', 'SE 605', 'SE 606']
        elif semester=='7':
            courseList = ['Internship']
            courseCode = ['SE 701']
        else:
            courseList = ['Project', 'Software Maintenance', 'Software Project Management', 'Machine Learning', 'Embedded Systems']
            courseCode = ['SE 801', 'SE 811', 'SE 803', 'CSE 837', 'CSE 823']
    else:
        courseList = ['Introduction to Software Engineering', 'Professional Ethics for Information Systems', 'Software Metrics']


    return render(request, 'gradesApp/coursePage.html', context={
        'courseList': courseList,
        'courseCode': courseCode
    })
