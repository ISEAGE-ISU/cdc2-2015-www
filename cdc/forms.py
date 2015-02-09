from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class TestimonialForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.Textarea)
    postedby = forms.CharField(max_length=1000)
