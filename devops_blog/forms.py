from django import forms
from devops_blog.models import blogmodel


class blogform(forms.ModelForm):
    class Meta():
        model = blogmodel
        fields = '__all__'
