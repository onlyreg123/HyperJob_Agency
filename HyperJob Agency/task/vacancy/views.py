from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views import View
from django.forms import ModelForm

from .models import Vacancy


class NewVacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['description']


class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancies.html', {'vacancies': vacancies})


class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        authorized_user = request.user.is_authenticated and request.user.is_staff
        if not authorized_user:
            return HttpResponseForbidden('<h1>403 (Forbidden)</h1>')

        form = NewVacancyForm(request.POST)
        if not form.is_valid():
            return HttpResponseForbidden('<h1>403 (Forbidden)</h1>')

        author = request.user
        description = form.cleaned_data['description']
        Vacancy.objects.create(author=author, description=description)
        return redirect('/home')
