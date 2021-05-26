from django.forms import ModelForm
from .models import Category, Tag, Author, Post

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'description', 'category', 'author', 'tags']
