# main/views.py
from django.shortcuts import redirect, render
from .constants import NAVIGATION_LINKS
from .forms import CustomUserCreationForm

def navigation_view(request):
    return render(request, 'home.html', {
        'urls': NAVIGATION_LINKS
    })

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})