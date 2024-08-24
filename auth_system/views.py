from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'auth_system/register.html'
    success_url = reverse_lazy('main:main-page')

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)
            if user.is_authenticated:
                return HttpResponseRedirect(self.success_url)
            else:
                return redirect("auth_system:login")

        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = "auth_system/login.html"
    redirect_authenticated_user = True
