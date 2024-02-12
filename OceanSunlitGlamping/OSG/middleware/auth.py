from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


# 檢查用戶是否已登入，未登入就跳到登入頁面
# 用戶發請求時，取得其cookie字串，看看是否存在session中
class AuthMiddleware(MiddlewareMixin):
    """中間件(堆疊執行)"""

    def process_request(self, request):
        # 0. 排除不須登入就能訪問的頁面
        # request.path_info 得到目前用戶請求的url
        if request.path_info in ['/login/', reverse('OSG:captcha')]:
            return

        # 1. 讀取送請求之用戶的session，如果能讀到，說明已登入，繼續往後訪問
        info_dict = request.session.get('info')
        if info_dict:
            return

        # 2. 沒有登入過，回到登入頁面
        return redirect('/login/')
