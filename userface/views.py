import string
import random
from django.core.files import File
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from zinnia.models.entry import Entry
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from Techword.settings import MEDIA_ROOT,ZINNIA_UPLOAD_TO
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required
def change(request):

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        make_a_slug=slugify(request.POST.get('title'))
        post = Entry(title=sanitize(request.POST.get('title')),
                    slug=sanitize(make_a_slug),
                    lead=sanitize(request.POST.get('lead')),
                    image=request.FILES.get('image'),
                    status=sanitize(request.POST.get('status')),
                    content=sanitize(request.POST.get('content')),
                    )
        post.save()
        make_a_slug = make_a_slug + str(post.pk)
        make_a_slug = slugify(make_a_slug)
        Artic = Entry.objects.get(id=post.pk)
        Artic.sites.set([Site.objects.get_current().pk])
        Artic.slug = make_a_slug
        Artic.authors.set([request.user.pk])
        Artic.save()
        return render(request, 'blogui/article.html', {'form': form})
    else:
        form = ArticleForm()
        return render(request, 'blogui/article.html', {'form': form })

@login_required
def AboutView(request):
	form = ArticleForm()
	return render(request, 'blogui/article.html', {'form': form})


def matter(request):
    return render(request,'user_profile/userprofile.html')

def userview(request):
    return render(request,'blogui/index.html')

def user_article_gallery(request):
    return render(request,'blogui/gallary.html')

def user_article_create(request):
    return render(request,'blogui/article.html')

def user_category_create(request):
    return render(request,'blogui/category.html')

def user_tag_create(request):
    return render(request,'blogui/tag.html')

def sanitize(text):
    cleared_text=''
    ch=0
    temp=''
    identify=0
    for word in text:
        if word=='<':
            ch=1
        if word=='>':
            ch=2
            temp+=word
        if ch==1:
            temp+=word
            # print(temp)
        if ch==2:
            if temp[0:7]=='<script' or temp[0:8]=='<section' or temp[0:4]=='<div' or temp[0:7]=='<navbar' or temp[0:4]=='<nav':
                cleared_text+='<pre style="color:white;background-color:black;"><!--Please Dont rape my baby -->'
                temp=''
            elif temp[0:8]=='</script'or temp[0:8]=='</sectio' or temp[0:5]=='</div' or temp[0:7]=='</navba' or temp[0:5]=='</nav':
                cleared_text+='</pre>'
                temp=''
            else:
                cleared_text+=temp
                temp=''
            ch=0
            continue
        if(ch==0):
            cleared_text+=word

    return cleared_text
