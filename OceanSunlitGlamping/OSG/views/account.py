from django.shortcuts import render, redirect
from django import forms

from OSG import models
from OSG.utils.bootstrapStyle import BootstrapForm
from OSG.utils.encrypt import md5


class LoginForm(BootstrapForm):
    username = forms.CharField(label='電子郵件',
                               widget=forms.TextInput(attrs={"type": "email", "placeholder": "電子郵件"}))
    password = forms.CharField(label='密碼',
                               widget=forms.PasswordInput(attrs={"type": "password", "placeholder": "密碼"}))

    def clean_password(self):
        return md5(self.cleaned_data.get('password'))


def login_view(request):
    """登入"""
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 驗證成功，獲取使用者輸入的資料
        # 去資料庫驗證是否正確
        # admin_obj = models.Admin.objects.filter(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password')).first()
        admin_obj = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_obj:
            form.add_error('password', '帳號或密碼錯誤')
            return render(request, 'login.html', {'form': form})

        # 帳號密碼正確
        # 網站生成隨機字串；寫到客戶端瀏覽器cookie中，再寫入到session中；
        request.session['info'] = {'id': admin_obj.id, 'username': admin_obj.username}
        return redirect('/admin/list/')

    return render(request, 'login.html', {'form': form})

