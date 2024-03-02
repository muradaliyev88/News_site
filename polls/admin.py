from django.contrib import admin
from .models import News,Kategory


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'body']

    class Meta:
        model = News

class KategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = Kategory


admin.site.register(News,NewsAdmin)
admin.site.register(Kategory,KategoryAdmin)
