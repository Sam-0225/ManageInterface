from django.urls import path
from OSG.views import index, admin, account

app_name = 'OSG'

urlpatterns = [
    path('', index.home_view, name='home'),  # 將首頁路徑映射到 home view

    # 管理員的管理
    path('admin/list/', admin.admin_list_view),
    path('admin/add/', admin.admin_add_view),
    path('admin/<int:nid>/edit/', admin.admin_edit_view),
    path('admin/<int:nid>/delete/', admin.admin_del_view),

    # 會員的管理


    # 登入
    path('login/', account.login_view),
]
