from django.shortcuts import render
from OSG import models
from OSG.utils.paginator import Paginator
import copy

def admin_list_view(request):
    """管理員列表"""

    # 搜尋
    data_dict = {}
    value = request.GET.get('q', '')
    if value is not None:
        data_dict['username__contains'] = value

    queryset = models.Admin.objects.filter(**data_dict)  # .order_by('-id')遞減排序

    # 分頁
    page_obj = Paginator(request, queryset)

    context = {
        'search_fields': value,
        'queryset': page_obj.page_queryset,  # 分完頁的資料
        'page_string': page_obj.html()       # 頁碼
    }
    return render(request, 'admin_list.html', context)

def admin_add_view(request):
    return render(request, 'admin_add.html')

