from django.urls import path
from .views import contatti

app_name = "forms_apps"

urlpatterns=[
    path('contattaci/', contatti, name='contatti'),
]