from django.forms import ModelForm

from notes_app.models import Profile, Note


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class NoteForm(ModelForm):
    class Meta:
        model=Note
        fields = '__all__'