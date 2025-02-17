
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.views import LoginView, LogoutView 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import login


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        print(form.errors)  # Debugging: Print errors in the terminal
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Auto-login after signup (optional)
        return super().form_valid(form)


# Custom Login View :
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Custom Logout View :
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
