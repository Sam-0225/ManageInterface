from django.shortcuts import render


def home(request):
    # 渲染模板並返回響應
    return render(request, 'index.html')
