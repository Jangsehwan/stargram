from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
# 자체에서 제공해주는 Form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserCreateForm, SignUpForm, LoginFrom

# from django.contrib.auth.models import User


def signup_view(request):
    # GET요청시 HTML응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    # POST요청시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            # 회원가입처리
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts/signup.html')


def login_view(request):
    # GET, POST분리
    if request.method == 'GET':
        # 로그인 html응답
        form = AuthenticationForm
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            # 비지니스 로직 처리 - 로그인처리
            login(request, form.user_cache)
            # 응답
            return redirect('index')
        else:
            # 비지니스 로직 처리 - 로그인실패
            # 응답
            return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    # 유효성검사 - login일경우 체크 , is_authenticated property라서 ()하지않아
    if request.user.is_authenticated:
        # 비지니스로직처리 - 로그아웃처리
        logout(request)
    # 응답
    return redirect('index')
