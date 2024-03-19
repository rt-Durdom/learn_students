from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    """Форма для отображения зачисленных на курс студентов."""
    model = Student
    fields = ('first_name', 'last_name', 'product', 'start_product')
