from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm


def home(request):
    return render(request, 'core/index.html')

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'core/person_list.html', {'persons': persons})

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'core/person_form.html', {'form': form})

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'core/person_form.html', {'form': form})

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'core/person_confirm_delete.html', {'person': person})

from rest_framework import viewsets
from .serializers import PersonSerializer

#rest
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

#consumir servicio 
#def consume_external_service(request):
#    response = requests.get('https://api.example.com/data')
#    data = response.json()
#    return render(request, 'external_data.html', {'data': data})

#modulo
from .services.external_service import get_external_data

def consume_external_service(request):
    data = get_external_data()
    return render(request, 'core/external_data.html', {'data': data})

#subir pdf 
from .models import PDFDocument
from .forms import PDFDocumentForm

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.save()
            print(pdf.pdf_file.path)
            return redirect('pdf_list')
    else:
        form = PDFDocumentForm()
    return render(request, 'core/upload_pdf.html', {'form': form})

def pdf_list(request):
    pdfs = PDFDocument.objects.all()
    return render(request, 'core/pdf_list.html', {'pdfs': pdfs})

#cambiar color pdf
from django.http import HttpResponse
from .services.pdf_utils import invert_pdf_colors
import os

def download_inverted_pdf(request, pdf_id):
    pdf = PDFDocument.objects.get(id=pdf_id)
    input_path = pdf.pdf_file.path
    output_path = os.path.join('inverted_pdfs', os.path.basename(input_path))
    invert_pdf_colors(input_path, output_path)
    with open(output_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='/pdf')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(output_path)}"'
        return response

