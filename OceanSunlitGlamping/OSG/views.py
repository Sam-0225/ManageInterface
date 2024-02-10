from django.shortcuts import render
from .models import SiteConfiguration

def home(request):
    # 獲取 SiteConfiguration 模型的實例
    site_config = SiteConfiguration.objects.first()

    # 將全局設定傳遞給模板
    context = {
        'site_name': site_config.site_name,
        'welcome_message': site_config.welcome_message,
        'contact_email': site_config.contact_email,
    }

    # 渲染模板並返回響應
    return render(request, 'index.html', context)