from django.shortcuts import render
from OSG import models


def admin_list(request):
    """管理員列表"""

    data_dict = {}
    value = request.GET.get('q')
    if value is not None:
        data_dict['username__contains'] = value

    queryset = models.Admin.objects.filter(**data_dict)  # .order_by('-id')遞減排序
    context = {
        'queryset': queryset,
        'search_fields': value
    }
    return render(request, 'admin_list.html', context)
