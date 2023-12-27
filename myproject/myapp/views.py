from django.shortcuts import render
from .models import Person


def people_list(request):
    people = Person.objects.all()
    return render(request, 'people_list.html', {'people': people})
