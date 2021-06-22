from django.urls import path

from tracker import views
from tracker.views import *


urlpatterns=[
    path('', index, name = 'index'),
    path('create/', create_expense, name = 'create expense'),
    path('edit/<int:pk>/', edit_expense, name = 'edit expense'),
    path('delete/<int:pk>/', delete_expense, name = 'delete expense'),
    path('profile/', profile_index, name = 'profile index'),
    path('profile/create/', create_profile, name = 'create profile'),
    path('profile/edit/', edit_profile, name = 'edit profile'),
    path('profile/delete/', delete_profile, name = 'delete profile'),
]
"""
http://localhost:8000/ - home page
http://localhost:8000/create - create expense page
http://localhost:8000/edit/:id - edit expense page
http://localhost:8000/delete/:id - delete expense page
http://localhost:8000/profile - profile page
http://localhost:8000/profile/edit - profile edit page
http://localhost:8000/profile/delete - delete profile page
"""