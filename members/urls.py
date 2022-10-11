from django.urls import path
from . views import UserEditView, PasswordsChangeView
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='members/change_password.html')),
    path('password_changed', views.password_changed, name='password_changed'),
    path('password_reset', views.password_reset, name='password_reset'),


]