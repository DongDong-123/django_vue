from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
import random
import time

from .models import Book
from .models import User

@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def del_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_id'))
        book.is_delete = 1
        book.save()
        response["msg"] = "success"
        response["error_num"] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def register(request):
    response = {}
    try:
        user = User()
        user.userid = str(random.randint(100,999)) + str(time.time()).replace(".", "")
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        print(user.username)
        print(user.password)

        user.save()
        response["msg"] = "success"
        response["error_num"] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter(is_delete=0)
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def search_book(request):
    response = {}
    try:
        book = Book.objects.filter(is_delete=0).filter(book_name__icontains=request.GET.get('book_name'))
        response['list'] = json.loads(serializers.serialize("json", book))
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

from django.middleware.csrf import get_token


@require_http_methods(["GET"])
def make_token(request):
    print('request',request, type(request))
    response = {}
    csrf_token = get_token(request)
    print(csrf_token)
    response["csrf_token"] = csrf_token
    return JsonResponse(response)


# @require_http_methods(["POST"])
def login(request):
    response = {}
    try:
        user = User.objects.get(username=request.POST.get('username'))
        if user:
            db_password = user.password
            login_password = request.POST.get('password')
            if db_password == login_password:
                response['msg'] = '登陆成功！'
                response['error_num'] = 0
            else:
                response['msg'] = '密码错误！'
                response['error_num'] = 0
        else:
            response['msg'] = '用户名错误！'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response, status=200)



@require_http_methods(["GET"])
def look_delete(request):
    response = {}
    try:
        book = Book.objects.filter(is_delete=1)
        response['list'] = json.loads(serializers.serialize("json", book))
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)




