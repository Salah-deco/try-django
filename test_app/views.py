from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def CreateStudentForm(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        print("is valid")

    context = {
        'form': form,
    }
    return render(request, 'student/studentform.html', context)