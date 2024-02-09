from django.urls import path, include
from .views import home

app_name = 'mainapp'

urlpatterns = [
    path('', home, name= 'home'),# 將首頁路徑映射到 home 視圖
]