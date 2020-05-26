from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Topic, Author, Course, Department
from django.db import models

class TopicAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Topic, TopicAdmin)
admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Department)

