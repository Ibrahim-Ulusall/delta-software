from django.contrib import admin
from . import models
# Register your models here.
class LessonAdminPanel(admin.ModelAdmin):
    list_display = ('title','create_date','update_date','slug')

admin.site.register(models.Lesson,LessonAdminPanel)