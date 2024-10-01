from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.predictor, name="Predictor"),
    # path('predict', views.formData, name="Formdata"),
]