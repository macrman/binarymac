from django.contrib import admin
from tutorials.models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}

admin.site.register(Tutorial, TutorialAdmin)
