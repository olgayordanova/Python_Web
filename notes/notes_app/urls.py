from django.urls import path

from notes_app.views import index, add_note, edit_note, delete_note, note_details, profile, profile_delete

urlpatterns =[
    path ( '', index, name='index' ),
    path ( 'add/', add_note, name='add note' ),
    path ( 'edit/<int:pk>/', edit_note, name='edit note' ),
    path ( 'delete/<int:pk>/', delete_note, name='delete note' ),
    path ( 'details/<int:pk>/', note_details, name='note details' ),
    path ( 'profile/', profile, name='profile' ),
    path ( 'profile/delete/', profile_delete, name='profile delete' ),
    # path ( 'create/profile/', create_profile, name='create profile' ),
]

"""


"""