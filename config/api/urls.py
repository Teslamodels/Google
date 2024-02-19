from django.urls import path
from .views import get_data, create_data, update_data, delete_data

urlpatterns = [
    path('data/', get_data, name='data'),
    path('create/', create_data, name='create'),
    path('edit/<slug:id>/', update_data, name='update'),
    path('delete/<slug:id>/', delete_data, name='delete'),
]