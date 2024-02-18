from django.urls import path
from .import views
urlpatterns = [
    path('add/', views.add_model, name="add_model"),
    path('edit/<int:id>', views.edit_task, name="edit_task"),
    path('delete/<int:id>', views.delete_task, name="delete_task"),
]