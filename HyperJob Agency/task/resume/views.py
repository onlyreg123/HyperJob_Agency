from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views import View
from django.forms import ModelForm

from .models import Resume


class NewResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['description']


class ResumeListView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resumes.html', {'resumes': resumes})


class NewResumeView(View):
    def post(self, request, *args, **kwargs):
        authorized_user = request.user.is_authenticated and not request.user.is_staff
        if not authorized_user:
            raise PermissionDenied

        form = NewResumeForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest('<h1>403 (Forbidden)</h1>')

        author = request.user
        description = form.cleaned_data['description']
        Resume.objects.create(author=author, description=description)
        return redirect('/home')
