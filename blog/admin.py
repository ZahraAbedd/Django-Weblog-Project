from django.contrib import admin

from .models import  Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified', )
    # ordering = ('status', )
    ordering = ('-status', )
admin.site.register(Post, PostAdmin)
# Register your models here.
