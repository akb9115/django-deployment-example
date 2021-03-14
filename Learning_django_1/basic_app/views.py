from django.shortcuts import render
from basic_app.models import student
from basic_app.forms import studentForm
# Create your views here.
def index(request):
    student_data = student.objects.all()
    return render(request,"basic_app/index.html",{'student':student_data})

def other(request):
    return render(request,"basic_app/other.html")

def relative(request):
    return render(request,"basic_app/relative_url_templates.html")

def studentRegs(request):
    form = studentForm()

    if request.method == "POST":
        form = studentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            student_data = student.objects.all()
            return render(request,"basic_app/index.html",{'student':student_data})
        else:
            print("ERROR!!FORM INVALID")
    return render(request,"basic_app/add_student.html",{'form':form})

def deleteStudent(request,roll):
    student_data = student.objects.get(roll = roll)
    student_data.delete()
    new_student_data = student.objects.all()
    return render(request,"basic_app/index.html",{'student':new_student_data})
