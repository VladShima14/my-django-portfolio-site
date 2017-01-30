from django.contrib import admin

# Register your models here.
from agro.models import Email, Post, SliderItem, Rewiew, Topic, Category, HomeItem

class EmailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'topic']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Email, EmailAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(SliderItem)
admin.site.register(Rewiew)
admin.site.register(Category, CategoryAdmin)
admin.site.register(HomeItem)