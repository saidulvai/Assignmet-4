from django.shortcuts import render
from TaskModel.models import Task_Model
def home(request):
    data = Task_Model.objects.all()
    return render(request, 'show.html', {'data' : data})