from django import forms
from .models import *
class Login(forms.Form):
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={'class':'form-control required'}))
    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control required'}))
class Edit(forms.ModelForm):
    class Meta:
        model=User
        fields=['password','name','address','phone']
        laebls={'password':'密码','name':'昵称','address':'地址','phone':'手机号码'}
        widgets={'password':forms.TextInput(attrs={'class':'form-control'}),'name':forms.TextInput(attrs={'class':'form-control'}),'address':forms.TextInput(attrs={'class':'form-control'}),'phone':forms.NumberInput(attrs={'class':'form-control'})}
class RegisterForm(forms.Form):
    username=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Password",max_length=128,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label="Password1", max_length=128,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    name=forms.CharField(label="name",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone=forms.CharField(label="Phone",max_length=128,widget=forms.NumberInput(attrs={'class':'form-control'}))
    address=forms.CharField(label="Address",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username=username)
        if len(filter_result) > 0:
            raise forms.ValidationError("当前邮箱已存在")
        return username
    def apassword(self,password,password1):
        print(self.cleaned_data)
        print(password,password1)
        if password!=password1:
            print()
            raise forms.ValidationError("输入的两次密码不一致")
        elif len(password)>16 or len(password)<8:
            raise forms.ValidationError("您的密码可能超过八位数或十六位数了")
        elif password.isalnum()==False:
            raise forms.ValidationError("您的密码含有非法字符")
        return password

