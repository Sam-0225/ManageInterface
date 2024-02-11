from django.urls import path
from OSG.views import index, admin

app_name = 'OSG'

urlpatterns = [
    path('', index.home, name='home'),  # 將首頁路徑映射到 home view

    #管理員的管理
    path('admin/list', admin.admin_list_view),
    path('admin/add', admin.admin_add_view),

    #會員的管理
]
