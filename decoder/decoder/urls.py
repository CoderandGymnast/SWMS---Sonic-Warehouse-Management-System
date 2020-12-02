"""decoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.auth import urls, views as auth_views
# from qr_bar_decoder import views
from . import views
from django.conf.urls.static import static

from urllib.parse import urlparse
from django.conf import settings

urlpatterns = [
	path("", views.landing, name="landing"),
	path('admin/', admin.site.urls),
	path("qr_bar_decoder/", include("qr_bar_decoder.urls")),
	path("accounts/", include("django.contrib.auth.urls")),
	# path(f"{urlparse('accounts/login/?next=').geturl()}<next>", auth_views.LoginView.as_view(), name="login"),
	# path("accounts/login/?next=<path:next>", auth_views.LoginView.as_view(), name="login"),  # Path converters: https://docs.djangoproject.com/en/3.1/topics/http/urls/#path-converters
	# re_path(r'^accounts/login/(?P<next>[1-9]|10)/$', auth_views.LoginView.as_view(), name="login"),
	# path("accounts/profile/", views.profile, name="profile"),
	# path("accounts/profile/", views.profile, name="profile"),
	path("accounts/logout/", views.logout, name="logout"),
	path("start/", views.start, name="start"),
	path("start/save", views.save, name="save"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
