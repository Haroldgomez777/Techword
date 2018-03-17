from django import forms
from django.forms import ModelForm
from django.forms import CharField
from django.forms import IntegerField ,DateTimeField, ImageField
from zinnia.models.entry import Entry
from django.utils.translation import ugettext_lazy as _
from zinnia.managers import DRAFT, HIDDEN, PUBLISHED

STATUS_CHOICES = ((DRAFT, _('draft')),
                  (HIDDEN, _('hidden')),
                  (PUBLISHED, _('published')))

class ArticleForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ArticleForm, self).__init__(*args, **kwargs)
	title = CharField(
						max_length=255,
						widget=forms.TextInput(attrs={
							'id': 'wer',
							'class':'form-control col-md-7 col-xs-12',
							'type': 'text'
							}))
	status = IntegerField( widget=forms.Select(
										choices=STATUS_CHOICES,
										attrs={'class': 'form-control' }
										))
	publication_date = DateTimeField (widget=forms.TextInput(attrs={
									'type': 'text',
									'id': 'single_cal1',
									'class': 'form-control col-md-7 col-xs-12',
									}))
	lead = CharField (
						widget=forms.Textarea(attrs={
									'type': 'textarea',
									'class': 'form-control col-md-7 col-xs-12'
									}))

	content = CharField (
						widget=forms.Textarea(attrs={
									'type': 'textarea',
									'class': 'form-control col-md-7 col-xs-12'
									}))
	image = ImageField(
						widget=forms.ClearableFileInput(attrs={
									'type': 'file',
									'class': ''
									})
						)
	class Meta:
		model = Entry
		exclude = ['id',
					'slug',
					'sites',
					'start_publication',
					'end_publication',
					'creation_date',
					'comment_enabled',
					'pingback_enabled',
					'trackback_enabled',
					'comment_count',
					'pingback_count',
					'trackback_count',
					'last_update',
					'authors',
					'related',
					'excerpt',
					'image_caption',
					'tags',
					'login_required',
					'password',
					'content_template',
					'detail_template',
					'categories',
					'featured',
				]


# Use exclude = instead of fields

"""
id="id_publication_date" name="publication_date" type="text"
"""
# id (AutoField) – Id
# title (CharField) – Title
# slug (SlugField) – Used to build the entry’s URL.
# status (IntegerField) – Status
# publication_date (DateTimeField) – Used to build the entry’s URL.
# start_publication (DateTimeField) – Start date of publication.
# end_publication (DateTimeField) – End date of publication.
# creation_date (DateTimeField) – Creation date
# last_update (DateTimeField) – Last update
# content (TextField) – Content
# comment_enabled (BooleanField) – Allows comments if checked.
# pingback_enabled (BooleanField) – Allows pingbacks if checked.
# trackback_enabled (BooleanField) – Allows trackbacks if checked.
# comment_count (IntegerField) – Comment count
# pingback_count (IntegerField) – Pingback count
# trackback_count (IntegerField) – Trackback count
# lead (TextField) – Lead paragraph
# excerpt (TextField) – Used for SEO purposes.
# image (ImageField) – Used for illustration.
# image_caption (TextField) – Image’s caption.
# featured (BooleanField) – Featured
# tags (TagField) – Tags
# login_required (BooleanField) – Only authenticated users can view the entry.
# password (CharField) – Protects the entry with a password.
# content_template (CharField) – Template used to display the entry’s content.
# detail_template (CharField) – Template used to display the entry’s detail page.