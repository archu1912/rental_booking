"""RentalBikes URL Configuration

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
from django.urls import path
from app import views as app_view
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.helloView, name='hello'),
    url(r'^$', app_view.HomePageView.as_view()),
    url(r'^about/$', app_view.AboutPageView.as_view()), # Add this /about/ route
    url(r'^vehicle/',include('vehicle.urls')),
    url(r'^customer/',include('customer.urls')),
    url(r'^booking/',include('booking.urls')),
    url(r'^inventory/',include('inventory.urls'))
]
