
from django.urls import path, include
from .views import person_list, person_create, person_update, person_delete, home, PersonViewSet, upload_pdf, pdf_list, download_inverted_pdf
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', person_list, name='person_list'),
    path('home/', home, name='home'),
    path('new/', person_create, name='person_create'),
    path('edit/<int:pk>/', person_update, name='person_update'),
    path('delete/<int:pk>/', person_delete, name='person_delete'),
    path('upload/', upload_pdf, name='upload_pdf'),
    path('pdfs/', pdf_list, name='pdf_list'),
    path('', include(router.urls)),
    path('download_inverted/<int:pdf_id>/', download_inverted_pdf, name='download_inverted_pdf'),
]
