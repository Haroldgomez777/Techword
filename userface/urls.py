from django.conf.urls import url
from userface import views


# /artic/
app_name = 'userface'
urlpatterns = [
    url(r'^$', views.AboutView, name='about'),
    url(r'^min$', views.matter),
    url(r'^home$',views.userview,name='home'),
    url(r'^uagallary$',views.user_article_gallery,name='gallary'),
    url(r'^article$',views.user_article_create,name='article'),
    url(r'^category$',views.user_category_create,name='category'),
    url(r'^tag$',views.user_tag_create,name='tag'),
    url(r'^addcategory$',views.add_category,name='addcategory'),
]