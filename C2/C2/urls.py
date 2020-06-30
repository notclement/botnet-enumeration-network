"""C2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.shortcuts import redirect


def redirect_root(request):
    return redirect('webui/')


urlpatterns = [
    path('', redirect_root),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('webui/', include('webui.urls'), name='webui'),
]
