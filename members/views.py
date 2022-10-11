from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import EditProfileForm, UserRegisterForm, PasswordChangingForm

class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_changed')

def password_changed(request):
    return render(request, 'members/password_changed.html', {})

def password_reset(request):
    return render(request, 'members/password_reset.html', {})

def password_reset_done(request):
    return render(request, 'members/password_reset_done.html', {})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'members/register.html', {'form': form})

class UserEditView(LoginRequiredMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'members/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


