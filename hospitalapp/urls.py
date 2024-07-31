"""
URL configuration for hospital project.

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
from django.urls import path,include
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup),
    path('1',views.signingup),
    path('2',views.logpg),
    path('3',views.login),
    path('4',views.doc_signingup),
    path('5/<u>',views.patient_profile),
    path('6/<u>',views.doctor_profile),
    path('7',views.user_logout),
]
