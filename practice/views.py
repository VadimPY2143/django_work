from django.shortcuts import render
from forms import LoginForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

    else:
        form = LoginForm
    return render(request, 'login.html', {'form': form})



