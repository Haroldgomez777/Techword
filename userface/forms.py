from django import forms
from django.forms import ModelForm
from zinnia.models.entry import Entry

class ArticleForm(ModelForm):
	class Meta:
		model = Entry
		fields = ['title','lead','status','image','content','publication_date']
