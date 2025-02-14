from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
python_pages = [
  {"title": "Official Python Tutorial",
   "url": "http://docs.python.org/3/tutorial/",
   "views": 64},
  # ...
]

def add_page(cat, title, url, views=0):
    p, created = Page.objects.get_or_create(category=cat, title=title)
    p.url = url
    p.views = views
    p.save()
    return p
