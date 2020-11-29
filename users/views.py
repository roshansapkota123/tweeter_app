from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = 'Successcully signed you up'

class UserUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class =  CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'update.html'
    success_message = 'successfully updated user'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)

class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'change_password.html'
    success_message = 'Sucessfully changed password'

class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'reset_password.html'
    success_message = 'Please check the email and open the reset link'
