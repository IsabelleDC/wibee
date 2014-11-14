from django.shortcuts import render, redirect
from collect.forms import PlaceForm


def home(request):
    return render(request, 'index.html')

def new_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect("/home")
    else:
        form = PlaceForm()

    data = {'form': form}
    return render(request, 'index.html', data)