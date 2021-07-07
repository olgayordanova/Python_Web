from django.shortcuts import render, redirect

from notes_app.forms import NoteForm, ProfileForm
from notes_app.models import Note, Profile


# def index(request):
#     if Note.objects.exists():
#         notes =  Note.objects.all()
#         context={
#             'notes': notes,
#         }
#         return render(request, 'index.html', context)
#     else:
#         return render(request, 'index.html')


# def index(request):
#     if Profile.objects.exists():
#         profile =  Profile.objects.all()[0]
#         notes = Note.objects.all()
#         # budget_left = profile.budget - sum(expense.price for expense in expenses)
#         context={
#             'profile': profile,
#             'notes': notes,
#             # 'budget_left': budget_left
#         }
#         return render(request, 'home-with-profile.html', context)
#     else:
#         return create_profile(request)

def index(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        notes = Note.objects.all()
        count_notes = len(notes)
        context = {
            'profile': profile,
            'notes': notes,
            'count_notes': count_notes
        }
        return render(request, 'home-with-profile.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home-with-profile.html')
            # return redirect('home-with-profile.html')
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)

def add_note(request):
    if request.method == 'GET':
        context = {
            'form': NoteForm (),
        }
        return render ( request, 'note-create.html', context )
    else:
        form = NoteForm ( request.POST )
        if form.is_valid ():
            form.save ()
            return redirect ( 'index' )
        context = {
            'form': form,
        }
        return render ( request, 'note-create.html', context )
    pass

def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'note': note,
            'form': NoteForm ( instance=note ),
        }
        return render ( request, 'note-edit.html', context )
    else:
        form = NoteForm ( request.POST, instance= note)
        if form.is_valid ():
            form.save ()
            return redirect ( 'index' )
        context = {
            'form': form,
        }
        return render ( request, 'note-edit.html', context )


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteForm ( instance=note )
        for name, field in form.fields.items():
            field.widget.attrs['disabled']=True #readonly  disabled
            form.save(commit=False)

        context = {
            'note': note,
            'form': form,
        }
        return render(request, 'note-delete.html', context)

    else:
        note.delete()
        return redirect('index')
    pass

# def get_list_recipe_ingredients (ingredients):
#     return ingredients.split(",")

def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': NoteForm ( instance=note ),
            'note': note,
        }
        return render ( request, 'note-details.html', context )
    else:
        pass


def profile(request):
    profile = Profile.objects.all()[0]
    notes = Note.objects.all()
    count_notes = len(notes)
    if profile:
        if request.method == 'GET':
            context = {
                'profile': profile,
                'notes':notes,
                'count_notes': count_notes
            }
            return render(request, 'profile.html', context)
        else:
            return redirect ( 'index' )

def profile_delete(request):
    profile = Profile.objects.all()[0]
    notes = Note.objects.all()
    for note in notes:
        note.delete()
    profile.delete()
    return redirect('index')

"""
def index(request):
    if Profile.objects.exists():
        profile =  Profile.objects.all()[0]
        notes = Note.objects.all()
        # budget_left = profile.budget - sum(expense.price for expense in expenses)
        context={
            'profile': profile,
            'notes': notes,
            # 'budget_left': budget_left
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)

def profile_index(request):
    profile = Profile.objects.all()[0]
    notes = Note.objects.all()
    # budget_left = profile.budget - sum(expense.price for expense in expenses)
    context = {
        'profile': profile,
        'notes': notes,
        # 'budget_left': budget_left
    }
    return render(request, 'profile.html', context)
    # else:
    #     form = ProfileForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    #     context = {
    #         'form': form
    #     }
    #     return render(request, 'home-no-profile.html', context)

def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(),
        }

        return render(request, 'home-no-profile.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'home-no-profile.html', context)
"""