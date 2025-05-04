from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import LearningEntryForm
from .models import LearningEntry
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.http import Http404

@login_required
def dashboard(request):
    user_entries = LearningEntry.objects.filter(
        user=request.user, 
        deleted_at__isnull=True
    )
    shared_entries = LearningEntry.objects.filter(
        shared_with=request.user, 
        deleted_at__isnull=True
    ).exclude(user=request.user)
    return render(request, 'dashboard.html', {
        'user_entries': user_entries,
        'shared_entries': shared_entries
    })

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = LearningEntryForm(request.POST, user=request.user)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('dashboard')
    else:
        form = LearningEntryForm(user=request.user)
    return render(request, 'create_entry.html', {'form': form})

@login_required
@require_POST
def toggle_entry_status(request, pk):
    entry = LearningEntry.objects.get(pk=pk)
    if entry.user != request.user:
        raise Http404
    entry.is_completed = not entry.is_completed
    entry.save()
    return redirect('dashboard')

@login_required
@require_POST
def delete_entry(request, pk):
    entry = LearningEntry.objects.get(pk=pk)
    if entry.user != request.user:
        raise Http404
    entry.soft_delete()
    return redirect('dashboard')

def logout_view(request):
    logout(request)
    return redirect('/')