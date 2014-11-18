from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# from collect.forms import PlaceForm
from collect.forms import EmailUserCreationForm


def home(request):
    return render(request, 'home.html')

# def first(request):
#     return render(request, 'first.html')

def index(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            user = form.save()
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
        return redirect("index")
    else:
        form = EmailUserCreationForm()

    return render(request, "index.html", {'form': form})
# def new_place(request):
#     if request.method == 'POST':
#         form = PlaceForm(request.POST, request.FILES)
#         if form.is_valid():
#             if form.save():
#                 return redirect("/home")
#     else:
#         form = PlaceForm()
#
#     data = {'form': form}
#     return render(request, 'index.html', data)