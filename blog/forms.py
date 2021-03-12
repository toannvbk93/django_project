from django import forms

class SearchForm(forms.Form):
    content_search = forms.CharField(label='Your keyword',
        widget=forms.TextInput(attrs={'class' : 'form-control mr-sm-2', 'type': 'search', 'placeholder': 'Enter your keyword', 'aria-label': 'search'}),
        max_length=100)