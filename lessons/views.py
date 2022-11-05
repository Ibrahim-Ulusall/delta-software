from django.shortcuts import render
from .models import Lesson
# Create your views here.

def index(request):
    context = Lesson.objects.all()
    return render(request,'lesson/index.html',context= {
        'lesson':context
    })