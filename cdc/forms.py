from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class TestimonialForm(forms.Form):
    text = forms.TextField(max_length=1000)
    postedby = forms.CharField(max_length=1000)
