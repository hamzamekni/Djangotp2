from django.urls import path

from .views import controleform1, controleform2

urlpatterns=[
    path('', controleform1, name='controleform1'),
    path('form', controleform2, name='controleform2'),
]