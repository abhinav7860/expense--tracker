from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense


# --------------------
# REGISTER
# --------------------
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            login(request, user)
            return redirect('dashboard')

    return render(request, 'register.html')


# --------------------
# DASHBOARD
# --------------------
@login_required
def dashboard(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        date = request.POST.get('date')

        if title and amount and float(amount) > 0 and category != "Select Category":
            Expense.objects.create(
                user=request.user,
                title=title,
                amount=amount,
                category=category,
                date=date
            )
        return redirect('dashboard')

    expenses = Expense.objects.filter(user=request.user)
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_entries = expenses.count()

    return render(request, 'dashboard.html', {
        'expenses': expenses,
        'total_expense': total_expense,
        'total_entries': total_entries,
    })


# --------------------
# DELETE
# --------------------
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(
        Expense,
        id=expense_id,
        user=request.user
    )
    expense.delete()
    return redirect('dashboard')


# --------------------
# UPDATE
# --------------------
@login_required
def update_expense(request, expense_id):
    expense = get_object_or_404(
        Expense,
        id=expense_id,
        user=request.user
    )

    if request.method == 'POST':
        expense.title = request.POST.get('title')
        expense.amount = request.POST.get('amount')
        expense.category = request.POST.get('category')
        expense.date = request.POST.get('date')
        expense.save()
        return redirect('dashboard')

    return render(request, 'update_expense.html', {'expense': expense})
def home(request):
    return render(request, 'home.html')