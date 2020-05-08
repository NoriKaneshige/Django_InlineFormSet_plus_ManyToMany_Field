from django.contrib import admin
from .models import Post, Tag

# these are for Post model and tag inline display in admin site
class TagInline(admin.TabularInline):
    model = Post.tag.through


class PostAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ('tag',)

admin.site.register(Post, PostAdmin)


# these are for Tag model and post inline display in admin site
class PostInline(admin.TabularInline):
    model = Post.tag.through


class TagAdmin(admin.ModelAdmin):
    inlines = [PostInline]


admin.site.register(Tag, TagAdmin)

