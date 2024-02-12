from django import forms


class BootstrapStyle:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 遍歷ModelForm中所有item的widget做設定
        for name, field in self.fields.items():
            # 無屬性就添加，有的話就保留屬性，新增值
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    'class': 'form-control',
                    'placeholder': field.label
                }


class BootstrapModelForm(BootstrapStyle, forms.ModelForm):
    pass


class BootstrapForm(BootstrapStyle, forms.Form):
    pass

