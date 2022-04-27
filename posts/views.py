from tkinter import Image
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Post


def index(reqeust):
    post_list = Post.objects.all().order_by('-created_at')  # Post 전체 데이터 조회
    context = {
        'post_list': post_list,
    }
    return render(reqeust, 'index.html', context)


def post_list_view(reqeust):
    post_list = Post.objects.all()  # Post 전체 데이터 조회
    # post_list = Post.objects.filter(writer=reqeust.user)  # Post.writer가 현재 로그인인것 조회

    context = {
        'post_list': post_list,
    }
    return render(reqeust, 'posts/post_list.html', context)


def post_detail_view(reqeust, id):
    return render(reqeust, 'posts/post_detail.html')


@login_required
def post_create_view(reqeust):
    if reqeust.method == 'GET':
        return render(reqeust, 'posts/post_form.html')
    else:
        image = reqeust.FILES.get('image')
        content = reqeust.POST.get('content')

        # db에 생성, 저장
        Post.objects.create(
            image=image,
            content=content,
            writer=reqeust.user,
        )
        return redirect('index')


def post_update_view(reqeust, id):
    return render(reqeust, 'posts/post_form.html')


def post_delete_view(reqeust, id):
    return render(reqeust, 'posts/post_confirm_delete.html')


def url_view(request):
    print('url_view()')
    data = {'code': '001', 'msg': 'OK'}
    # return JsonResponse(data)
    return HttpResponse('<h1>url_view</h1>')


# 뷰에서 데이터를 받는법
# 1.path variable지정 2.query parameter stream ?, key:value형태 3.form으로 입력
# url 패턴으로 변수를 정의해 놓은경우는 parameter로 추가해서 받을수 있고
# query로는 request.GET으로 받을수있어
def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)


def function_view(request):
    print(f'request.method: {request.method}')

    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')


class ClassView(ListView):
    model = Post
    ordering = ['-id']
    # template_name = 'cbv_view.html'


def function_list_view(request):
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list': object_list})
