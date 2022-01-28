from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #message.debug
            #message.info
            #message.success
            #message.warning
            #message.error
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acount created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
