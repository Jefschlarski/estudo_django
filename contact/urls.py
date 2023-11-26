from django.urls import path
from contact.views import views 
from contact.views import forms 

app_name = 'contact'

urlpatterns = [
    path('', views.index, name = 'index'),
    
    path('search/', views.search, name = 'search'),

    # contact CRUD
    path('<int:contact_id>/', views.contact, name = 'contact'),
    path('create/', forms.create, name = 'create'),
]
