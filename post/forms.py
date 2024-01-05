from django import forms

class CreatePost(forms.Form):
  title = forms.CharField(max_length=255)
  content = forms.CharField(widget=forms.Textarea)
  pub_date = forms.DateTimeField()
