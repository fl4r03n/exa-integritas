from django import forms
from .models import Person, PDFDocument

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'phone', 'occupation']

class PDFDocumentForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'pdf_file']