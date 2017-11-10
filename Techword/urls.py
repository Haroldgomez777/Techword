"""Techword URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from userface.views import AboutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('zinnia.urls')),
	url(r'^comments/', include('django_comments.urls')),


    url(r'^login/', include('app.urls')),
    # url(r'^about/$', TemplateView.as_view(template_name="checker.html")),
    url(r'^artic/$', AboutView.as_view()),
    url(r'^app/', include('app.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/',views.profile, name='profile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)