from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PersonWithHobbie(Person):
    hobbie = models.CharField(max_length=100, blank=True)
    
class PDFDocument(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

