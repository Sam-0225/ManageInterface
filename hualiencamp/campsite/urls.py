from django.urls import path
from .views import campsite_detail

urlpatterns = [
    path('<int:campsite_id>/', campsite_detail, name='campsite_detail'),
    # 其他 URL 規則根據需求添加
]