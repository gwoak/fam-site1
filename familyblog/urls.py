from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from members import views as members_views
# no register option on front end

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    # path('register/', members_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('blog/', include('blog.urls')),
    path('members/', include('members.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
           
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)