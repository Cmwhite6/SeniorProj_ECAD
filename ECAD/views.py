from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from vpython import *
import os

from .forms import FileForm
from .models import File

class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')

    else:
        form = FileForm()
    return render(request, 'upload.html', {
        'form' : form

    })

def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html',{
        'files' : files
    })

def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')

def renderSTL(request, pk):
    if request.method == 'POST':
        fileinfo = File.objects.get(pk=pk)
        fd = fileinfo.file.open( mode='rb')
        tris = []
        if False:
            pass
        else:
            fd.seek(0)
            flist = fd.readlines()
            vs = []
            for line in flist:
                FileLine = line.split()
                if FileLine[0] == b'facet':
                    N = vec(float(FileLine[2]), float(FileLine[3]), float(FileLine[4]))
                elif FileLine[0] == b'vertex':
                    vs.append(vertex(pos=vec(float(FileLine[1]), float(FileLine[2]), float(FileLine[3])), normal=N,
                                     color=color.white))
                    if len(vs) == 3:
                        tris.append(triangle(vs=vs))
                        vs = []
    return compound(tris)
 #   return redirect('file_list')