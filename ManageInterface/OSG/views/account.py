from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse

from OSG import models
from OSG.utils.bootstrapStyle import BootstrapForm
from OSG.utils.captcha import check_captcha
from OSG.utils.encrypt import md5
from io import BytesIO


class LoginForm(BootstrapForm):
    username = forms.CharField(label='帳號',
                               widget=forms.TextInput(attrs={'type': 'text', 'placeholder': '帳號'}),
                               required=True)
    password = forms.CharField(label='密碼',
                               widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': '密碼'}),
                               required=True)
    captcha = forms.CharField(label='驗證碼',
                              widget=forms.TextInput(attrs={'type': 'text', 'placeholder': '請輸入驗證碼', 'id': 'captcha'}),
                              required=True)

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

        # 驗證碼校驗
        user_input_captcha = form.cleaned_data.pop('captcha')
        system_captcha = request.session.get('captcha', '')
        if user_input_captcha.upper() != system_captcha.upper():
            form.add_error('captcha', '驗證碼錯誤')
            return render(request, 'login.html', {'form': form})

        # 去資料庫驗證是否正確 admin_obj = models.Admin.objects.filter(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password')).first()
        admin_obj = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_obj:
            form.add_error('password', '帳號或密碼錯誤')
            return render(request, 'login.html', {'form': form})

        # 帳號密碼正確
        # 網站生成隨機字串；寫到客戶端瀏覽器cookie中，再寫入到session中；
        request.session['info'] = {'id': admin_obj.id, 'username': admin_obj.username}
        request.session.set_expiry(60*60*24*7)  # session保持7天
        return redirect(reverse('OSG:admin_list'))

    return render(request, 'login.html', {'form': form})


def captcha_view(request):
    """生成圖片驗證碼"""
    # 呼叫pillow函數，生成圖片
    img, code_string = check_captcha()
    # 寫到session中，以便後續取得並校驗
    request.session['captcha'] = code_string
    # 給session設定100秒超時
    request.session.set_expiry(100)
    print(code_string)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue(), content_type='image/png')


def logout_view(request):
    """登出"""
    request.session.flush()
    return redirect(reverse('OSG:login'))
