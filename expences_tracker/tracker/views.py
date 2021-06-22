from django.shortcuts import render, redirect

# Create your views here.
from tracker.forms import ProfileForm, ExpenseForm
from tracker.models import Profile, Expense

"""
http://localhost:8000/ - home page
http://localhost:8000/create - create expense page
http://localhost:8000/edit/:id - edit expense page
http://localhost:8000/delete/:id - delete expense page
http://localhost:8000/profile - profile page
http://localhost:8000/profile/edit - profile edit page
http://localhost:8000/profile/delete - delete profile page
"""
def index(request):
    if Profile.objects.exists():
        profile =  Profile.objects.all()[0]
        expenses = Expense.objects.all()
        budget_left = profile.budget - sum(expense.price for expense in expenses)
        context={
            'profile': profile,
            'expenses': expenses,
            'budget_left': budget_left
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)

def profile_index(request):
    profile = Profile.objects.all()[0]
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(expense.price for expense in expenses)
    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left
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

def edit_profile(request):
    profile = Profile.objects.all()[0]

    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
        }

        return render(request, 'profile-edit.html', context)
    else:
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'profile-edit.html', context)

def delete_profile (request):
    profile = Profile.objects.all()[0]
    expenses = Expense.objects.all()

    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
        }
        return render(request, 'profile-delete.html', context)
    else:
        for expense in expenses:
            expense.delete()
        profile.delete()
        return redirect('index')


def create_expense(request):
    if request.method=='GET':
        context = {
            'form': ExpenseForm()
        }
        return render(request, 'expense-create.html', context)
    else:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render ( request, 'home-with-profile.html', context )

def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpenseForm(instance=expense),
        }

        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'expense': expense,
            'form': form,
        }

        return render(request, 'expense-edit.html', context)

def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpenseForm(instance=expense),
        }

        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('index')
