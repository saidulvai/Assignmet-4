from django.shortcuts import render, redirect
from .import forms
from .import models
# Create your views here.
def add_model(request):
    if request.method == 'POST':
        model_form = forms.Task_ModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('add_model')
    else:
        model_form = forms.Task_ModelForm()
    return render(request, 'add_model.html', {'form' : model_form})

def edit_task(request, id):
    post = models.Task_Model.objects.get(pk=id)
    model_form = forms.Task_ModelForm(instance=post)
    if request.method == 'POST':
        model_form = forms.Task_ModelForm(request.POST, instance=post)
        if model_form.is_valid():
            model_form.save()
            return redirect('show')
    return render(request, 'add_model.html', {'form' : model_form})

def delete_task(request, id):
    post = models.Task_Model.objects.get(pk=id)
    post.delete()
    return redirect('show')