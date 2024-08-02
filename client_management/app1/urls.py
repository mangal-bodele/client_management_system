from django.urls import path
from .views import add_employee,show_employee,update_employee,delete_employee

urlpatterns =[
    path('add/',add_employee, name='add_url'),
    path('show/',show_employee, name='show_url'),
    path('update/',update_employee, name='update_url'),
    path('delete/',delete_employee, name='delete_url')
]