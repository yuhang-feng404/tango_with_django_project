from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    """
    Customizing the admin panel for the Page model.
    """
    list_display = ('title', 'category', 'url', 'views')  # Show title, category, URL, views in the admin panel
    list_filter = ('category',)  # Filter by category
    search_fields = ('title', 'url')  # Allow search by title or URL

class CategoryAdmin(admin.ModelAdmin):
    """
    Customizing the admin panel for the Category model.
    """
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from name

# Register models in Django Admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
