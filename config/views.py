from django.shortcuts import redirect

def index(request):
    #로그인O
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    #로그인X
    else:
        return redirect("users:login")