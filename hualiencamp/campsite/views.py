from django.shortcuts import render
from .models import Campsite

def campsite_detail(request, campsite_id):
    try:
        campsite = Campsite.objects.get(pk=campsite_id)
        # 找到了露營區，可以進行相應的處理
    except Campsite.DoesNotExist:
        # 沒有找到露營區的情況，進行相應的處理
        pass
    return render(request, 'detail.html', {'campsite': campsite})