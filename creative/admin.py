from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Idea, Project


class IdeaAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Idea


class IdeaAdmin(admin.ModelAdmin):
    form = IdeaAdminForm

admin.site.register(Idea, IdeaAdmin)
admin.site.register(Project)
