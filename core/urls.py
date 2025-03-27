from django.urls import path
from .views import Home, Add_Student, Delete_Student, Edit_student

urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('add-student',Add_Student.as_view(), name="add_student"),
    path('edit-student/<int:id>', Edit_student.as_view(), name='edit_student'),
    path('delete-student',Delete_Student.as_view(), name="delete_student")
]