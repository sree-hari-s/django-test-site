
from django import forms
from django.forms import ModelForm
from test_app.models import UserInfo
class user_UpdateForm(ModelForm):
    class Meta:
        model=UserInfo
        fields ="__all__"
        required_fields = ['username','number','email','password']
        widgets={
            'number':forms.IntegerField(attrs={'class':' form-control mb-3 '}),
            'email': forms.TextInput(attrs={'class':' form-control mb-3 '}),
            'username': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'password': forms.TextInput(attrs={'class':'form-control mb-3'}) 
            }
        labels={
            'email':'email',
            'number':'number',
            'username':'Username',
            'password':'Password'    
        }
    