from django.forms import ModelForm

from tracker.models import Profile, Expense


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        fields = '__all__'


