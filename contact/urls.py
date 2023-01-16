from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addcontact/', views.add_contact, name='addcontact'),
    path('profile/<str:pk>', views.contact_profile, name='profile'),
    path('editcontact/<str:pk>', views.edit_contact, name='editcontact'),
    path('deletecontact/<str:pk>', views.delete_contact, name='deletecontact'),
]
