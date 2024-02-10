from django.shortcuts import render

def admin_list(request):
    """管理員列表"""

    return render(request, 'admin_list.html')