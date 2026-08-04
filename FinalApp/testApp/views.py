from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'testApp/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(
        request,
        'testApp/register.html',
        {'form': form}
    )


@login_required
def profile(request):
    return render(request, 'testApp/profile.html')