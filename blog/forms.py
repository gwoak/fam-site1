from django import forms
from . models import Post, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
# this function ensures we get an up to date sorted category choices dropdown
# with title case style after adding a new category
    def __init__(self, *args, **kwargs):
        choices = Category.objects.all().values_list('name', 'name')
        choice_list = []
        for item in choices:            
            choice_list.append(item)
        choice_list.sort()
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ChoiceField(choices=choice_list, widget = forms.Select(
            attrs = {'class': 'form-control', 'style': 'text-transform: capitalize;'}))
   
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet', 'date_created')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'style': 'text-transform: capitalize;'}),            
            'body': CKEditorUploadingWidget(),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'date_created': forms.DateTimeInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'title_tag': 'Tag label that appears on the browser tab - change if desired',
            'snippet': 'Extract for summary page: max 255 characters',
            'date_created': 'Date created - change if desired',
        }

class EditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        choices = Category.objects.all().values_list('name', 'name')
        choice_list = []
        for item in choices:            
            choice_list.append(item)
        choice_list.sort()
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ChoiceField(choices=choice_list, widget = forms.Select(
            attrs = {'class': 'form-control', 'style': 'text-transform: capitalize;'}))
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'header_image', 'body', 'snippet', 'date_created')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': CKEditorUploadingWidget(),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'date_created': forms.DateTimeInput(attrs={'class': 'form-control'}),

        }