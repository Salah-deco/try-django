from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

# login via AuthenticationForm
def login_view(request):
    # add feature: next url after login
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


# simple authentication
# def login_view(request):
#     # print(dir(request))
#     # if request.user.is_authenticated:
#     #     return render(request, 'accounts/already-logged-in.html', {})
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # print(username, password)

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             context = {"error": "Invalid username or password"}
#             return render(request, "accounts/login.html", context)
#         login(request, user)
#         return redirect('admin/')
#     return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    return render(request, 'accounts/logout.html', {})
