from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
# Register your models here.
from .models import Post, DemoPost
admin.site.register(Post)

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = DemoPost
        fields = '__all__'
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
admin.site.register(DemoPost, PostAdmin)