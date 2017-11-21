from django.conf.urls import url
from userface import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.

    url(r'^$', views.AboutView, name='about'),
    url(r'^min$', views.matter),
]