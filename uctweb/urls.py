# Authors; Yaseen Hull, Laeeq Diedericks, Thobeka Gumede
# Project; Capstone SITPG
# Date; September 2019

"""uctweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from users import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_view.cover, name='cover'),
    path('register/', user_view.register, name='register'),
    path('login/', user_view.CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile_form/', user_view.edit_profile, name='profile_form'),
    path('status_form/', user_view.profile_status, name='status_form'),
    path('delete_form/', user_view.withdrawal, name='delete_form'),
    path('student_home/', user_view.home, name='student_home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)