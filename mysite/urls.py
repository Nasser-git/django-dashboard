"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from mysite.core import views as view_core
from mysite.dashboard import views as view_dashboard

urlpatterns = [
    path('', view_core.home, name='home'),
    path('signup/', view_core.signup, name='signup'),
    # path('dashboard/', view_dashboard.dashboard_page, name='dashboard'),
    # path('dashboard/upload/', view_dashboard.upload, name='upload'),
    # path('dashboard/viewdata/', view_dashboard.viewdata, name='flights'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('dashboard/', include("mysite.dashboard.urls")),
    path('map/', include("mysite.map.urls")),

    path('admin/', admin.site.urls),

]
