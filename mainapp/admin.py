from django.contrib import admin

from mainapp import models as mainapp_models


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "num", "title", "deleted"]
