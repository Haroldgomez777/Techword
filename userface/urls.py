from django.conf.urls import url
from userface import views

app_name = 'userface'
urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.

    url(r'^$', views.AboutView, name='about'),
    url(r'^min$', views.matter),
    url(r'^home$',views.userview,name='home'),
    url(r'^uagallary$',views.user_article_gallery,name='gallary'),
    url(r'^article$',views.user_article_create,name='article'),
    url(r'^category$',views.user_category_create,name='category'),
    url(r'^tag$',views.user_tag_create,name='tag'),
]