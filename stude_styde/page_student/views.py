from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, UpdateView

from .models import Student
# Create your views here.


class StudentListView(ListView):
    """Класс вывода зачисленых на курс студентов."""
    model = Student
    template_name = 'page_student.html'

    def get_queryset(self):
        return Student.objects.select_related(
            'author', 'product', 'start_product', 'price_product').filter(
                student_is_paid=True
            )


class StudentListUpdateView(UpdateView):
    

'''def post_form(request):
    template_name = 'page_student.html'
    context = {}

    return render(request, template_name, context)'''