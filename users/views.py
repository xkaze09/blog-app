from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# register
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
