from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Student
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Create your views here.
class Home(View):
    def get(self, request):
        data = Student.objects.all().order_by('-id')
        return render(request, 'pages/home.html',{'data': data}) 
    
class Add_Student(View):
    def get(self, request):
        return render(request, 'pages/add-student.html')
    
    def post(self, request):
        name = request.POST.get('name')
        roll = request.POST.get("roll")
        city = request.POST.get("city")
        age = request.POST.get("age")

        Student.objects.create(name=name, roll=roll, city=city, age=age)
        return redirect('home')
    
class Edit_student(View):
    def get(self, request, id):
       student = get_object_or_404(Student, id=id)
       context = {'student': student}
       return render(request, 'pages/edit-student.html', context)
    
    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        city = request.POST.get('city')
        age = request.POST.get('age')

        if not name or not roll or not city or not age:
            return render(request, 'pages/edit-student.html', {
                'student': student,
                'error': "All fields are required!"
            })

        student.name = name
        student.roll = roll
        student.city = city
        student.age = age
        student.save()

        return redirect('home') 



class Delete_Student(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('home')


