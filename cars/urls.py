from django.urls import path
from . import views

urlpatterns = [
    path('cars/',views.CarsViewset.as_view()),
    path('cars/<int:id>',views.CarsViewset.as_view())
]
