from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

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
