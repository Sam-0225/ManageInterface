from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render, redirect
from OSG import models
from OSG.utils.paginator import Paginator
from OSG.utils.encrypt import md5
from django import forms
from OSG.utils.bootstrap import BootstrapModelForm


def admin_list_view(request):
    """管理員列表"""

    # 搜尋
    data_dict = {}
    value = request.GET.get('q', '')
    if value is not None:
        data_dict['username__contains'] = value

    queryset = models.Admin.objects.filter(**data_dict)  # .order_by('-id')遞減排序

    # 分頁
    page_obj = Paginator(request, queryset)

    context = {
        'search_fields': value,
        'queryset': page_obj.page_queryset,  # 分完頁的資料
        'page_string': page_obj.html()  # 頁碼
    }
    return render(request, 'admin_list.html', context)


class AdminModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),  # 參數放render_value=True，可使送出後欄位內容不消失
        label='確認密碼'
    )

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        conf_password = md5(self.cleaned_data['confirm_password'])
        if self.cleaned_data['password'] != conf_password:
            raise ValidationError('密碼不一致')
        return conf_password


def admin_add_view(request):
    """新增管理員"""
    title = '新增管理員'
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'data_add.html', {'form': form, 'title': title})

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'data_add.html', {'form': form, 'title': title})


def admin_edit_view(request, nid):
    """編輯管理員"""
    # 物件 / None
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {'msg': '資料不存在'})
    title = '編輯管理員'
    if request.method == 'GET':
        form = AdminModelForm(instance=row_object) # 使用與新增一樣的ModelForm
        return render(request, 'data_add.html', {'form': form, 'title': title})
    form = AdminModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'data_add.html', {'form': form, 'title': title})

