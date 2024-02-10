from django.urls import path
from OSG.views import index, admin

app_name = 'OSG'

urlpatterns = [
    path('', index.home, name='home'),  # 將首頁路徑映射到 home view

    path('admin/list', admin.admin_list),
]
