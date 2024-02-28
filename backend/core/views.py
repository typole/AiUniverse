from django.shortcuts import render

# Create your views here.

# backend/myapp/views.py

from django.http import JsonResponse


def first_request(request):
    # 处理前端请求逻辑
    data = {"message": "Hello from Django backend!"}
    return JsonResponse(data)


def home_page(request):
    data = {"message": "this is a homepage!!!"}
    return JsonResponse(data)
