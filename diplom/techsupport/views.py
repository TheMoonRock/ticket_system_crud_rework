from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Problem
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserLoginForm
from django.contrib.auth.models import User

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('user_problem')

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['request_from_date', 'name_of_problem', 'description_of_problem']

def warning_list(request):
    all_problem = Problem.objects.all()
    return HttpResponse(all_problem)

def create_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
            return redirect('techsupport:profile')
    else:
        form = ProblemForm()
    
    return render(request, 'create_problem.html', {'form': form})

def profile_view(request):
    return render(request, 'authreg/profile.html')

@login_required
def user_problem(request):
    user_problem = Problem.objects.filter(user=request.user)
    return render(request, 'user_problem.html', {'user_problem': user_problem})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Problem, Feedback
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required

@login_required
def feedback_create(request, problem_id):
    problem = get_object_or_404(Problem, id_request=problem_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.problem = problem
            feedback.user = request.user
            feedback.save()
            return redirect('techsupport:profile')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form, 'problem': problem})
