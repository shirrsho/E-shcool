from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import MaterialForm
from .models import Material


def material_list(request):
    materials = Material.objects.all()
    return render(request, 'upload/material_list.html', {
        'materials': materials
    })

def upload_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/materials/materials')
    else:
        form = MaterialForm()
    return render(request, 'upload/upload_material.html', {
        'form': form
    })
