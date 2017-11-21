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

@login_required
def change(request):

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            post = Entry(title=request.POST.get('title'),
                        slug=slugify(request.POST.get('title')),
                        lead=request.POST.get('lead'),
                        image=request.FILES.get('image'),
                        status=request.POST.get('status'),
                        content=request.POST.get('content'),
                        )
            post.save()
            Artic = Entry.objects.get(id=post.pk)
            Artic.sites=[Site.objects.get_current().pk]
            Artic.authors = [request.user.pk]
            Artic.save()
            return render(request, 'userface/use_artic_form.html', {'form': form})
    else:
        form = ArticleForm()
        return render(request, 'userface/use_artic_form.html', {'form': form })

@login_required
def AboutView(request):
	form = ArticleForm()
	return render(request, 'userface/use_artic_form.html', {'form': form})


def matter(request):
    return render(request,'user_profile/userprofile.html')