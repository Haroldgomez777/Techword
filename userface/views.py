import string
import random
from django.core.files import File
from django.shortcuts import render
from django.utils import timezone
from django.utils.html import *
from django.views.generic import TemplateView
from zinnia.models.entry import Entry
from zinnia.models import Category
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from Techword.settings import MEDIA_ROOT,ZINNIA_UPLOAD_TO
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from django.http import JsonResponse

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
    return escape(text)


def add_category(request):
    make_a_slug = slugify(request.POST.get('title'))
    categor = Category(title=request.POST.get('title'),
    slug=sanitize(make_a_slug))
    categor.save()
    make_a_slug = make_a_slug + str(categor.pk)
    make_a_slug = slugify(make_a_slug)
    secategory = Category.objects.get(id=categor.pk)
    secategory.slug = make_a_slug
    secategory.save()
    return JsonResponse(categor.pk, safe=False)


