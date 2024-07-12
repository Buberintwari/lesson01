from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
# Create your views here.

def register_view (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
            form = UserCreationForm()
    return render(request,"users/register.html",{ "form": form })
