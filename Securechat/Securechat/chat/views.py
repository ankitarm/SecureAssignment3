from django.contrib.auth import login
from django.shortcuts import render,redirect

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'chat/frontpage.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'chat/register.html', {'form': form})
