from django.contrib import admin

from website.models import Category, Post, Tag, Author

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post)



