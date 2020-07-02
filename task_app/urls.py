from django.urls import path,include
from . import views

urlpatterns = [
    path('view_data',views.view_data,name='view_data' ),
]